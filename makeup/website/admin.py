from django.contrib import admin
from website.models import ContactModel, ServicesModel, AppointmentModel, BookingModel, TimingModel


# Register your models here.
admin.site.register(ContactModel)
admin.site.register(ServicesModel)
admin.site.register(AppointmentModel)
admin.site.register(BookingModel)
admin.site.register(TimingModel)
