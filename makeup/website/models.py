from django.db import models

class ContactModel(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.fname
    
class BookingModel(models.Model):
    username = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phone = models.IntegerField()
    phone = models.IntegerField(blank=True, null=True) 
    email = models.EmailField()
    prices = models.IntegerField()                                            
    services = models.CharField(max_length=50)                             
    # contact = models.ForeignKey("ContactModel", on_delete=models.CASCADE)        
    
    def __str__(self):
        return self.username
    

class ServicesModel(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class AppointmentModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    time = models.DateField(auto_now_add=True)
    date = models.DateField()

    def __str__(self):
        return self.name
 
