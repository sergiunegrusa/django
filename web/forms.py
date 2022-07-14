from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(max_length=120, label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Your description'})
    )
    class Meta: 
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ]


class RawProductForm(forms.Form):
    title =forms.CharField(max_length=120, widget=forms.Textarea(attrs={'placeholder': 'deescription'}))
    description = forms.CharField( 
        max_length=250, 
        required=False,
        widget= forms.Textarea(
            attrs={
                'placeholder': 'deescription',
                'class': 'form-control',
                'id': 'my_dashId_text_area',
                'rows': 20,
                'cols': 20,
            }
        )
    )
    price = forms.DecimalField(initial=199.99)
