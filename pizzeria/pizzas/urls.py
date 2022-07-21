from django.urls import path
from . import views 

## Helping django distinguish this urls.py from other with the same name
app_name = 'pizzas'  

# List of pages
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Showing all the orders
    path('orders/', views.orders, name='orders'),

    # Details for each order
    path('orders/<int:order_id>/', views.order, name='order')
]