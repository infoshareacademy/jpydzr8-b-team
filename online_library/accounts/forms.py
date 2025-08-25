from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MyRegisterForm(UserCreationForm):
    username = forms.CharField(required=True, max_length=25, widget=forms.TextInput(attrs={'placeholder': 'enter your username'}))
    first_name = forms.CharField(required=True, max_length=25, widget=forms.TextInput(attrs={'placeholder': 'enter your first name'}))
    last_name = forms.CharField(required=True, max_length=25, widget=forms.TextInput(attrs={'placeholder': 'enter your last name'}))
    email = forms.EmailField(required=True, max_length=25, widget=forms.TextInput(attrs={'placeholder': 'enter your email'}))
    password1 = forms.CharField(required=True, label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'enter your password'}))
    password2 = forms.CharField(required=True, label='Verify password', widget=forms.PasswordInput(attrs={'placeholder': 'enter your first name'}))

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
