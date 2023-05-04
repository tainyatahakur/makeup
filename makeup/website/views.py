from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from website.models import ContactModel
from website.forms import ContactForm
from django.contrib.auth import authenticate,  login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from website.models import BookingModel, TimingModel
from makeup.settings import EMAIL_HOST_USER
from website.forms import BookingForm
from website.models import ServicesModel
from website.forms import ServicesForm, AppointmentForm
from django.http import HttpResponse
import random
from django.core.mail import send_mail
from django.core import serializers
from website.forms import CreateUserForm
from django.http import JsonResponse
from website.models import AddBlog, CustomUser
from website.forms import AddBlogForm, CustomUserForm
from django.contrib.auth.decorators import login_required


def index(request):
    results = ""
    search = ""
    if request.method == "POST":
        search = request.POST.get('search')
        print("Search: ", search)
        # query = request.POST.get('search')
        if search:
            searchres = ServicesModel.objects.filter(name__icontains=search)
            datas = serializers.serialize("json", searchres)
            print("res: ", results)
            return render(request, 'website/search.html', {'datas': datas})
        else:
            data = None
    context = {'results': results, 'query': search}
    return render(request, 'website/index.html')


def homepage(request):
    # results = ""
    # search = ""
    if request.method == "GET":
        search = request.GET.get('abc')
        print("Searched: ", search)
        # query = request.POST.get('search')
        if search:
            searchres = ServicesModel.objects.filter(name__icontains=search)
            datas = serializers.serialize("json", searchres)
            # print("res: ", results)
            return render(request, 'website/search.html', {'datas': datas})
        else:
            data = None
    context = {}
    return render(request, 'website/homepage.html', context)


def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            print("Form Saved")
            messages.success(request, 'Contact Us Successfully')

            return redirect("homepage")
        else:
            print("Form Error: ", form.errors)
    context = {'form': form, }

    return render(request, 'website/contact.html', context)


def signup(request):
    form = CreateUserForm()
    customform = CustomUserForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        contact1 = request.POST.get('contact1')
        contact2 = request.POST.get('contact2')
        dod = request.POST.get('dod')
        print("Dod: ", dod)
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        otp = request.POST.get('otp')
        print('otp', otp)
        print('username: ', username)
        user = authenticate(email=email, password1=password1, password2=password2, address1=address1, dod=dod,
                            address2=address2, contact1=contact1, contact2=contact2, city=city, state=state, zip=zip)

        form = CreateUserForm(request.POST)
        customform = CustomUserForm(request.POST)
        user = authenticate(request, username=username, password=password1)

        print(customform)
        if form.is_valid():
            if customform.is_valid():
                random_numbers = random.randint(111111, 999999)
                print("Signup Done")
                # send_mail("User Data: ", f"OTP: {random_numbers}", EMAIL_HOST_USER, [
                #     email], fail_silently=True)
                messages.success(request, 'Sign Up Successfully')
                customform.save()
                user = form.save()
                login(request, user)
                print("Form2 save")
                return redirect('homepage')
                # return render(request, 'website/verification.html', {"otp": random_numbers})
            else:
                print("Form2 Error: ", customform.errors)
            # form.save()
            # print("Form Saved")
            user = form.cleaned_data.get("username")
            messages.success(request, "Account created for " +
                             user + " successfully")
            # response = JsonResponse({"success":True})
            return redirect("homepage")                 

        else:
            print("Invalid Form", form.errors)
            messages.success(request, form.errors)

    return render(request, "website/signup.html")


def signin(request):
    if request.method == 'POST':

        email = request.POST.get('email')
        print("Email: ", email)
        pass1 = request.POST.get('password')
        print("Password: ", pass1)
        username = User.objects.get(email=email).username
        print("u: ", username)
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            messages.success(request, "login successfully")
            return redirect('booking')

        else:
            print("User None")
        # login(request, user)
    # otp = request.POST.get('otp')
    # print('otp', otp)
    # user = authenticate(request, username=username, password=pass1)
    # print("User: ", user)
    # if user is not None:
    #     login(request, user)
    #     random_numbers = random.randint(111111, 999999)
    #     print("login Done")
    #     send_mail("User Data: ", f"OTP: {random_numbers}", EMAIL_HOST_USER, [email] , fail_silently=True)

        # messages.success(request, 'OTP sent successfully on your registered email')
    #     if request.user.is_superuser:
    #         return redirect('dashboard')
    #     return render(request, 'website/verification.html', {"otp": random_numbers})
    # else:
    #     print('form error ')
    #     messages.error(request, "Wrong Credentials")
    #     return redirect('index')

    return render(request, "website/signin.html")                


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('index')


@login_required
def booking(request):
    form = BookingForm()
    user = request.user
    userdata = CustomUser.objects.get(username=user)
    data = ServicesModel.objects.all()

    if request.method == "POST":
        form = BookingForm(request.POST)
        print(form)
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        services = request.POST.get('services')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        datentime = request.POST.get('datentime')
        time = request.POST.get('time')
        # time = TimingModel.objects.get(id=time)

        # total_payment = request.POST.get('total_payment')
        # services = json.dumps(se)
        # print("Services: ", services)
        # booking = BookingModel(fname=fname,lname=lname,address=address,state=state,zip=zip,datentime=datentime, phone=phone, email=email,  time=time,  services=services,)
        # booking.save()
        print('time: ', time)
        if form.is_valid():
            form.save()
            print("Form Saved")
            messages.success(request, "Your Booking is done Successfully" )

            return redirect("Your_booking")
        else:
            print("Form Error: ", form.errors)
    context = {'form': form, 'data': data, 'userdata': userdata}
    return render(request, 'website/booking.html', context)


def services(request):
    form = ServicesForm()

    if request.method == "POST":
        form = ServicesForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            print("Form Saved")
            return redirect("/")
        else:
            print("Form Error:", form.errors)
        context = {'form': form}
        return render(request, 'website/services.html', context)
    return render(request, 'website/services.html')


def appointment(request):
    form = AppointmentForm
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            print("Form Saved")
    else:
        print("Form Error:", form.errors)
    context = {'form': form, }

    name = request.POST.get('name')
    email = request.POST.get('email')
    date = request.POST.get('date')
    time = request.POST.get('time')
    # return HttpResponse('Appointment booked successfully!')
    return render(request, 'website/appointment.html')   


# def portfolio(request):
#     items = Portfolio.objects.all()
#     return render(request, 'website/portfolio.html', {'items': items})

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print("Email: ", email)
        random_numbers = random.randint(111111, 999999)
        print("Signup Done")
        send_mail("User Data: ", f"OTP: {random_numbers}", EMAIL_HOST_USER, [
                  email], fail_silently=True)
        messages.success(
            request, 'OTP sent successfully on your registered email')
        return render(request, 'website/new_password.html', {'otp': random_numbers, 'email': email})

    return render(request, 'website/forgot_password.html')


def search(request):
    results = ""

    if request.method == "POST":
        search = request.POST.get('search')
        print("Searched: ", search)
        # query = request.POST.get('search')
        if search:
            searchres = ServicesModel.objects.filter(name__icontains=search)
            datas = serializers.serialize("json", searchres)
            # print("res: ", results)                                       -
            return render(request, 'website/search.html', {'datas': datas})
        else:
            data = None
    # context = {'results': results, 'query': search}

    return render(request, 'website/search.html')                   


def GetBookingDatentime(request):
    if request.method == "POST":
        date = request.POST.get("date")
        # time = request.POST.get("time")

        print("Date: ", date)
        # print("Time: ", time)
        times = BookingModel.objects.filter(datentime=date)
        bookingTime = []
        for i in times:
            # print(i.name)
            # print(i.date)
            # print(i.time)
            bookingTime.append(i.time)
        print("Booking Time: ", bookingTime)
        alltimings = TimingModel.objects.all()
        allslots = []
        for i in alltimings:
            allslots.append(i)

        result = [value for value in allslots if value not in bookingTime]
        print("Result: ", result)
        if result == []:
            result = allslots
            print("Empty: ", result)

        bookingTimes = serializers.serialize('json', result)
        print("bookingTimes: ", bookingTimes)
        if BookingModel.objects.filter(datentime=date).exists():
            amount = "Time Slot is already Taken"
            print(amount)
            return JsonResponse({'amount': amount, 'times': bookingTimes}, status=200)

        else:
            amount = "Ready To Go"
            print(amount)
            return JsonResponse({'amount': amount, 'times': bookingTimes}, status=200)
    else:
        amount = "Ready To Go"
        return JsonResponse({'amount': amount}, status=200)


def Your_booking(request):
    data = BookingModel.objects.filter(username=request.user.username)
    context = {'data': data}
    return render(request, 'website/your_booking.html', context)


def addblog(request):
    form = AddBlogForm()

    if request.method == "POST":
        form = AddBlogForm(request.POST, request.FILES)

        title = request.POST['title']
        if AddBlog.objects.filter(title=title).exists():
            raise Exception("Blog Title Already Exists")

        if form.is_valid():
            form.save()
            # return redirect("blogs_index")

    context = {'form': form}
    return render(request, 'website/addblog.html', context)


def AllBlogs(request):
    blog = AddBlog.objects.all()
    context = {'blog': blog}
    return render(request, 'website/blogs.html', context)


def Readblog(request, id):
    blogs = AddBlog.objects.get(id=id)
    read = {'blogs': blogs}
    return render(request, 'website/readblogs.html', read)
