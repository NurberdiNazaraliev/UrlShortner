from django import forms
from .models import short_url

class UrlForm(forms.ModelForm):
    class Meta:
        model = short_url
        fields = ['long_url']

class ShortUrlForm(forms.ModelForm):
    class Meta:
        model = short_url
        fields = ['short_url']