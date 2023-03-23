from django.contrib import admin
from website.models import ContactModel, ServicesModel, AppointmentModel, BookingModel


# Register your models here.
admin.site.register(ContactModel)
admin.site.register(ServicesModel)
admin.site.register(AppointmentModel)
admin.site.register(BookingModel)
