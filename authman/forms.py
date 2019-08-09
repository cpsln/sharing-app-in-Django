from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserSignupForm(UserCreationForm):
    CHOICES=[('uploader','uploader'),
         ('downloader','downloader')]
    user_type = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'email']

