from django import forms
from .models import Student
from django.contrib.auth import get_user_model
from django.forms import ModelForm, TextInput


class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'student_id', 'email', 'age')
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'student_id': forms.NumberInput(attrs={'class': "form-control", 'type': 'number', 'min': '0'}),
            'email': TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': "form-control", 'type': 'number', 'min': '0'}),
        }