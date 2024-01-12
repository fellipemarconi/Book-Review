from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from booklist.models import Book

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
    
class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=3,
        max_length=50,
        required=True,
        error_messages={'min_length': 'Please, add more than 3 letters.'},
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 
            }
        )
    )
    last_name = forms.CharField(
        required=True,
        min_length=3,
        max_length=50,
        error_messages={'min_length': 'Please, add more than 3 letters.'},
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 
            }
        )
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'readonly': True, 
            }
        ))
    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )
    password2 = forms.CharField(
        label='Confirm Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text='Use the same password as before',
        required=False,
    )
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username',
        )
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        
    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        
        password = cleaned_data.get('password1')
        
        if password:
            user.set_password(password)
            
        if commit:
            user.save()
            
        return user
    
    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2', 
                    ValidationError('Your password and confirmation password do not match.'
                    , code='invalid'))
        return super().clean()
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email
        
        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('Email is already registered', code='invalid')
                )
        return email
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        
        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error('password1', ValidationError(errors))
                
        return password1
    
class BookForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    description = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    author = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    genre = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    year = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={'class': 'form-control'}
        )
    )
    picture = forms.FileField(
        required=True,
        widget=forms.FileInput(
            attrs={'accept': 'image/*', 'class': 'form-control'}
        )
    )
    class Meta:
        model = Book
        fields = (
            'title', 'author', 'genre',
            'year', 'description', 'picture',
        )