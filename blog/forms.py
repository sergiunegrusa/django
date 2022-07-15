from django import forms

from .models import Article

class ArticleModelForm(forms.ModelForm):
    title = forms.CharField(max_length=120, label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Title'})
    )
    text = forms.CharField( 
        max_length=250, 
        required=False,
        widget= forms.Textarea(
            attrs={
                'placeholder': 'description',
                'class': 'form-control',
                'id': 'my_dashId_text_area',
                'rows': 20,
                'cols': 20,
            }
        )
    )
    class Meta: 
        model = Article
        fields = [
            'title',
            'text',
    ]