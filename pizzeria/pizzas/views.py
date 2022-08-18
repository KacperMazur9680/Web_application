from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Pizza, Topping
from .forms import Pizza_Form, Topping_Form

def check_order_taker(order, request):
    """Checking if said order is associated with loged in employee"""
    if order.order_taker != request.user:
        raise Http404

def index(request):
    """Home page for the Pizzeria"""
    return render(request, 'pizzas/index.html')

@login_required
def orders(request):
    """Page for orders, each employee will see only their orders"""
    orders = Pizza.objects.filter(order_taker=request.user).order_by('date_added')
    context = {'orders': orders}
    return render(request, 'pizzas/orders.html', context )

@login_required
def order(request, order_id):
    """Showing the loged in employee the details of hes orders"""
    order = get_object_or_404(Pizza, id=order_id)
    check_order_taker(order, request)

    toppings = order.topping_set.all()
    context = {'order': order, 'toppings': toppings}
    return render(request, 'pizzas/order.html', context)

@login_required
def new_order(request):
    """Adding a new order"""
    if request.method != 'POST':
        form = Pizza_Form()
    else:
        form = Pizza_Form(data=request.POST)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.order_taker = request.user
            new_order.save()
            return redirect('pizzas:orders')
    
    context = {'form': form}
    return render(request, 'pizzas/new_order.html', context)

@login_required
def new_toppings(request, pizza_id):
    """Adding toppings to an order"""
    order = get_object_or_404(Pizza, id=pizza_id)
    check_order_taker(order, request)

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

@login_required
def edit_toppings(request, topping_id):
    """Editing the toppings of an order"""
    toppings = get_object_or_404(Topping, id=topping_id)
    order = toppings.pizza
    check_order_taker(order, request)

    if request.method != 'POST':
        form = Topping_Form(instance=toppings)
    else:
        form = Topping_Form(instance=toppings, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizzas:order', order_id=order.id)
    
    context = {'toppings': toppings, 'order': order, 'form': form}
    return render(request, 'pizzas/edit_toppings.html', context)