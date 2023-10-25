from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    student_id = forms.CharField(max_length=8, required=False, help_text='Optional.')

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'student_id', 'password1', 'password2',)
