from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Pizza, Topping
from .forms import Pizza_Form, Topping_Form

def index(request):
    """Home page for the Pizzeria"""
    return render(request, 'pizzas/index.html')

@login_required
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

def new_order(request):
    """Adding a new order"""
    if request.method != 'POST':
        form = Pizza_Form()
    else:
        form = Pizza_Form(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizzas:orders')
    
    context = {'form': form}
    return render(request, 'pizzas/new_order.html', context)

def new_toppings(request, pizza_id):
    """Adding toppings to an order"""
    order = Pizza.objects.get(id=pizza_id)

    if request.method != 'POST':
        form = Topping_Form()
    else:
        form = Topping_Form(data=request.POST)
        if form.is_valid():
            new_toppings = form.save(commit=False)
            new_toppings.pizza = order
            new_toppings.save()
            return redirect('pizzas:order', order_id = pizza_id)

    context = {'order': order, 'form': form}
    return render(request, 'pizzas/new_toppings.html', context)

def edit_toppings(request, topping_id):
    """Editing the toppings of an order"""
    toppings = Topping.objects.get(id=topping_id)
    order = toppings.pizza

    if request.method != 'POST':
        form = Topping_Form(instance=toppings)
    else:
        form = Topping_Form(instance=toppings, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizzas:order', order_id=order.id)
    
    context = {'toppings': toppings, 'order': order, 'form': form}
    return render(request, 'pizzas/edit_toppings.html', context)