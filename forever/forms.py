import email
from pyexpat import model
from unicodedata import name
from django import forms
from .models import Contact
from django.forms import ModelForm

#class ContactForm(forms.Form):
#    name = forms.CharField(label='Nume',max_length= 50)
#    email = forms.EmailField(label="E-mail")
#    mesaj = forms.CharField(label='Mesaj',widget=forms.Textarea(attrs={'rows':'10','cols':'80'}))
    
    
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields= ["name","email","mesaj"]
        
