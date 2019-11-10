from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label = "First Name")
    last_name = forms.CharField(label = "Last Name", required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name' ,'username', 'email', 'password1', 'password2']