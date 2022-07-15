from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(max_length=120, label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Title'})
    )
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
    class Meta: 
        model = Product
        fields = [
            'title',
            'description',
            'price',
    ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not 'CFE' in title:
            raise forms.ValidationError('This is not a valid title')
        else:
            return title
    
    def clean_description(self, *args, **kwargs):
        description = self.cleaned_data.get('description')
        if not 'news' in description:
            raise forms.ValidationError('This is not a valid description')
        else:
            return description


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
