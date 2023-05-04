from django.contrib import admin
from website.models import ContactModel, ServicesModel, AppointmentModel, BookingModel, TimingModel, AddBlog, CustomUser


# Register your models here.
admin.site.register(ContactModel)
admin.site.register(ServicesModel)
admin.site.register(AppointmentModel)
admin.site.register(BookingModel)
# admin.site.register(TimingModel)
class TimingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name'] 

admin.site.register(TimingModel, TimingAdmin)

admin.site.register(AddBlog)
admin.site.register(CustomUser)


