from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 
            }
        ))
    first_name = forms.CharField(
        min_length=3,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 
            }
        ))
    last_name = forms.CharField(
        min_length=3,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 
            }
        ))
    
    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name',
            'email', 'password1', 'password2',
        )
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Email is already registered', code='invalid')
            )
        return email