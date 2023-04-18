from website.models import ContactModel
from django.forms import ModelForm
from website.models import BookingModel
from website.models import ServicesModel, AppointmentModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



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




