from django import forms
from django.forms import ModelForm
from appModelForm.models import feedback


class feedbackForm(ModelForm):

    def clean_name(self):
        name = self.cleaned_data["name"]
        if len(name) < 1:
            raise forms.ValidationError("Name is too short!")
        return name

    class Meta:
        model = feedback
        fields = ["name", "email", "desc"]
        labels = {'name': 'Enter Name', 'desc': 'Enter Description',
                  'email': 'Enrer Email'}
