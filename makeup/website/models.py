from django.db import models

class ContactModel(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.fname
    
class BookingModel(models.Model):
    # username = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    phone = models.IntegerField()
    email = models.EmailField()
    #prices = models.IntegerField()                                            
    services = models.CharField(max_length=50) 
    state = models.CharField(max_length=50) 
    city = models.CharField(max_length=50)
    zip = models.IntegerField()
    datentime = models.DateField()                         
    # contact = models.ForeignKey("ContactModel", on_delete=models.CASCADE)        
    
    def __str__(self):
        return self.fname
    

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
 
