from django import forms
from django.forms import ModelForm
from .models import  *
from django import forms

# class feedbackForm(forms.Form):
#     name = forms.CharField(max_length=50)
#     email = forms.EmailField()  
#     desc = forms.CharField(widget=forms.Textarea)

class feedbackForm(ModelForm):
    class Meta:
        model = feedback
        fields = ["name", "email", "desc"]
        labels = {'name':'Enter Name', 'desc':'Enter Description', 'email':'Enrer Email'}
