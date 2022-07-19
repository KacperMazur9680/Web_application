from django.urls import path
from . import views

## Helping django distinguish this urls.py from other with the same name
app_name = 'pizzas'  

# List of pages
urlpatterns = [
    # Home page
    path('', views.index, name='index')
]