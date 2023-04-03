from django.urls import path,include
from website import views

urlpatterns = [
path('', views.index, name="index" ),
path('contact/', views.contact, name ='contact'),
path('signin/', views.signin, name = 'signin'),
path('signup/', views.signup, name = 'signup'),
path('signout/', views.signout, name = 'signout'),
path('booking/', views.booking, name ='booking'),
# path('search/', views.search, name = 'search'),
path('services/', views.services, name = 'services'),
path('appointment/', views.appointment, name = 'appointment'),
# path('portfolio/', views.portfolio, name = 'portfolio'),
path('forgot-password/', views.forgot_password, name='forgot_password'),
path('Search/', views.search, name ='Search'),


]       