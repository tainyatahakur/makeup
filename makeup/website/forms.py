from website.models import ContactModel
from django.forms import ModelForm
from website.models import BookingModel
from website.models import ServicesModel, AppointmentModel



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



