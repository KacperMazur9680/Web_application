from django.urls import path, include
from . import views

app_name = 'employees'
urlpatterns = [
    # Including the default auth urls.
    path('', include('django.contrib.auth.urls')),
    
    # Page for registering an employee
    path('register/', views.register, name='register')
]