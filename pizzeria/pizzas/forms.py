from django import forms
from .models import Pizza, Topping

class Pizza_Form(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['order']
        labels = {'order': ''}
        widgets = {'order': forms.Textarea(attrs={'rows': 1})}
    
class Topping_Form(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ['ingredients']
        labels = {'ingredients': ''}
        widgets = {'ingredients': forms.Textarea(attrs={'cols': 80})}
