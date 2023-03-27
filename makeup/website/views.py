from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from website.models import ContactModel
from website.forms import ContactForm
from django.contrib.auth import authenticate,  login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from website.models import BookingModel
from website.forms import BookingForm
from website.models import ServicesModel
from website.forms import ServicesForm, AppointmentForm
from django.http import HttpResponse


def index(request):
    return render(request, 'website/index.html')


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


def signup(request):
    if request.method == 'POST':
        # username = request.POST.get('username')
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = user.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(
            request, "Your Account has been successfully created.")
        # return redirect('signin')
        return render(request, 'website/signup.html')
    return render(request, 'website/signup.html')


def signin(request):
    if request.method == 'POST':

        email = request.POST.get('email')
        print("Email: ", email)
        pass1 = request.POST.get('password')
        print("Password: ", pass1)
        username = None  # set a default value for username
        try:
            username = User.objects.get(email=email).username
        except User.DoesNotExist:
            pass  # handle the error here
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

    #     messages.success(request, 'OTP sent successfully on your registered email')
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

    if request.method == "POST":
        form = BookingForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            print("Form Saved")
            # return redirect("/")
        else:
            print("Form Error: ", form.errors)
    context = {'form': form}
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


