from django import forms
from .models import Car


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('title', 'model', 'category', 'year', 'image', 'price')

