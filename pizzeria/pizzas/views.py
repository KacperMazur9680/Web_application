from django.shortcuts import render
from .models import Pizza

def index(request):
    """Home page for the Pizzeria"""
    return render(request, 'pizzas/index.html')

def orders(request):
    """Page for orders"""
    orders = Pizza.objects.order_by('date_added')
    context = {'orders': orders}
    return render(request, 'pizzas/orders.html', context )

def order(request, order_id):
    """Showing the details of each order"""
    order = Pizza.objects.get(id=order_id)
    toppings = order.topping_set.all()
    context = {'order': order, 'toppings': toppings}
    return render(request, 'pizzas/order.html', context)