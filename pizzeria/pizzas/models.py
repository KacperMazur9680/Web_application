from django.db import models
from django.contrib.auth.models import User

class Pizza (models.Model):
    order = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    order_taker = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.order

class Topping (models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    ingredients = models.TextField(default=str())
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.ingredients
