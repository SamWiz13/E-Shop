from django import forms
from multiupload.fields import MultiFileField
from .models import Product

class NewProductForm(forms.ModelForm):
    images = MultiFileField(label='Product Images', max_num=5, min_num=1)

    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'address', 'category', 'phone_number', 'tg_username']

    def save(self, request, commit=True):
        product =self.instance
        product.author = request.user
        super().save(commit)
        return product
    

class ProductForm(forms.ModelForm):
    images = MultiFileField(label='Product Images', max_num=5, min_num=1)

    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'address', 'category', 'phone_number', 'tg_username']

   
    