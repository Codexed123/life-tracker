from django import forms
#from django.contrib.auth.models import User Recurring Error
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class TemporaryField(forms.Form):
    username = forms.CharField(max_length=100, label="Username", widget=forms.TextInput(attrs={
        'class': 'field_1',
        'placeholder': ' Enter your username',
    }))
    password = forms.CharField(max_length=100, label="Password", widget=forms.PasswordInput(attrs={
        'placeholder': ' Enter your password',
        'class': 'field_2',
    }))

class SignUp_Field(UserCreationForm):
    password1 = forms.CharField(
        label="Password:",
        widget=forms.PasswordInput,
        help_text=""
    )

    password2 = forms.CharField(
        label="Password confirmation:",
        widget=forms.PasswordInput,
        help_text=""
    )
    username = forms.CharField(label="Username", widget=forms.TextInput, help_text="")

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ["username", "password1", "password2"]