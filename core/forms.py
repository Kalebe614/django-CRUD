from django import forms
from .models import ProductModel

class ProductModelForm(forms.ModelForm):

    class Meta:
        model = ProductModel
        fields = ['name', 'price','description','activity','image']

        labels = {
            'name': 'Name',
            'price': 'Price',
            'description': 'Description',
            'activity': 'Active',
            'image': 'Image',
                }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name Product'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price Product'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'activity': forms.CheckboxInput(),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }