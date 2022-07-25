from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Registering a new employee"""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_employee = form.save()
            login(request, new_employee)
            return redirect('pizzas:index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)