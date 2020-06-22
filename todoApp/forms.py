from django import forms
from .models import *


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'complete']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'complete']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'complete': forms.CheckboxInput()
        }