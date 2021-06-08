from django import forms
from way.models import *


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category()
        fields = "__all__"


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product()
        fields = "__all__"
        labels = {
            "name": "Enter name"
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order()
        fields = "__all__"
        labels = {
            "name": "Enter name"
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User()
        fields = "__all__"
        labels = {
            "first_name": "Enter name"
        }
