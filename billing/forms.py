from django import forms
from .models import Item, Bill

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'price', 'description']

class BillForm(forms.ModelForm):
    items = forms.ModelMultipleChoiceField(queryset=Item.objects.all())

    class Meta:
        model = Bill
        fields = ['items']

class ItemEditForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'price', 'description']
