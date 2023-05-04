from django.db import models
from ckeditor.fields import RichTextField


class ContactModel(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.fname


class TimingModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ServicesModel(models.Model):
    name = models.CharField(max_length=50)
    prices = models.IntegerField()

    def __str__(self):
        return self.name

    
class BookingModel(models.Model):
    username = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    services = models.ForeignKey(ServicesModel, on_delete=models.CASCADE)
    state = models.CharField(max_length=50) 
    zip = models.IntegerField()
    datentime = models.DateField() 
    time = models.ForeignKey(TimingModel, on_delete=models.CASCADE) 
    # amount = models.IntegerField(default=0)                  
    
    def __str__(self):
        return self.fname
    



class AppointmentModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    time = models.DateField(auto_now_add=True)
    date = models.DateField()

    def __str__(self):
        return self.name


class AddBlog(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField()
    pub_date = models.DateField(auto_now=True)
    category = models.CharField(max_length=200, blank=True)

    content = RichTextField()
    author= models.CharField(max_length=150, default="Priyanka")
    readtime = models.IntegerField()
    # dexc = models.TextField()
    # play = models.ForeignKey(Playlist, on_delete=models.CASCADE)

    # like = models.ManyToManyField(User)

    def __str__(self):  
        return self.title



class CustomUser(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password1 = models.CharField(max_length=100)
    dod = models.DateField()
    password2 = models.CharField(max_length=100)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    contact1 = models.IntegerField()
    contact2 = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.IntegerField()
    


    def __str__(self):
        return self.fname