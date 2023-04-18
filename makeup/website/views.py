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
    return render(request, 'website/homepage.html')

def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            print("Form Saved")
            # return redirect("/")
        else:
            print("Form Error: ", form.errors)
    context = {'form': form, }
    
    return render(request, 'website/contact.html', context)


def Signup(request):
    form = CreateUserForm()

    username = request.POST.get('username')
    email = request.POST.get('email')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    print(username)
    print(email)

    if request.method=='POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            print("Form Saved")
            user = form.cleaned_data.get("username")
            messages.success(request, "Account created for "+ user+ " succesfully")
            # response = JsonResponse({"success":True})
            user = authenticate(request, username=username, password=password1)
            if user is not None:
                login(request, user)
                messages.success(request, "login successfully")
                return redirect('homepage')
                

        else:
            print("Invalid Form", form.errors)
            response = JsonResponse({"error":form.errors})
            response.status_code = 403
            return response
            
    return render(request, 'website/signup.html', {'form':form})


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
            return redirect('homepage')
            
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

        #messages.success(request, 'OTP sent successfully on your registered email')
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


def booking(request):
    form = BookingForm()
    data= ServicesModel.objects.all()

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
            # return redirect("/")
        else:
            print("Form Error: ", form.errors)
    context = {'form': form,'data': data}
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
        send_mail("User Data: ", f"OTP: {random_numbers}", EMAIL_HOST_USER, [email] , fail_silently=True)
        messages.success(request, 'OTP sent successfully on your registered email')
        return render(request, 'website/new_password.html', {'otp': random_numbers, 'email': email})

    return render(request, 'website/forgot_password.html')  



def search(request):
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
    # return render(request, 'home/search.html', context)
    # return render(request, 'website/search.html', context)
    # return JsonResponse(data, safe=False)
    return render(request, 'website/search.html', {'result': data})



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
            return JsonResponse({'amount' : amount, 'times': bookingTimes}, status=200)

        else:
            amount = "Ready To Go"
            print(amount)
            return JsonResponse({'amount' : amount, 'times': bookingTimes}, status=200)
    else:
        amount = "Ready To Go"
        return JsonResponse({'amount' : amount}, status=200)

def Your_booking(request):
    data= BookingModel.objects.all()
    context = {'data':data}
    return render(request,'website/your_booking.html', context)