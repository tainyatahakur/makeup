from website.models import ContactModel
from django.forms import ModelForm
from website.models import BookingModel
from website.models import ServicesModel, AppointmentModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import AddBlog
from website.models import CustomUser




class ContactForm(ModelForm):
    class Meta:
        model = ContactModel
        fields = "__all__"

class BookingForm(ModelForm):
    class Meta:
        model = BookingModel
        fields = "__all__"

class ServicesForm(ModelForm):
    class Meta:
        model = ServicesModel
        fields = "__all__"

class AppointmentForm(ModelForm):
    class Meta:
        model = AppointmentModel
        fields = "__all__"

class CreateUserForm(UserCreationForm):
    # phone_no = forms.CharField(max_length = 10)
    class Meta:
        model = User
        fields = ["username","email","password1", 'password2']


class AddBlogForm(ModelForm):
    class Meta:
        model = AddBlog
        fields = "__all__"


class CustomUserForm(ModelForm):
    # phone_no = forms.CharField(max_length = 10)
    class Meta:
        model = CustomUser
        fields = ["fname", "lname", "username","email","password1", "password2", "address1", "address2", "contact1", "contact2", "city", "state", "zip", 'dod']
