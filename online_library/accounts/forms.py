from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserDetails

class MyRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=25, required=True)
    first_name = forms.CharField(max_length=25, required=True)
    last_name = forms.CharField(max_length=25, required=True)
    email = forms.EmailField(max_length=50, required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class ProfileForm(forms.ModelForm):
    city = forms.CharField(required=False)
    street = forms.CharField(required=False)
    house_number = forms.CharField(required=False)
    postal_code = forms.CharField(required=False)
    hobbies = forms.CharField(required=False, widget=forms.Textarea)
    date_of_birth = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date"}))

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            try:
                details = self.instance.accounts_details
                self.fields["city"].initial = details.city
                self.fields["street"].initial = details.street
                self.fields["house_number"].initial = details.house_number
                self.fields["postal_code"].initial = details.postal_code
                self.fields["hobbies"].initial = details.hobbies
                self.fields["date_of_birth"].initial = details.date_of_birth
            except UserDetails.DoesNotExist:
                pass

    def save(self, commit=True):
        user = super().save(commit=commit)
        details, _ = UserDetails.objects.get_or_create(user=user)
        details.city = self.cleaned_data.get("city") or ""
        details.street = self.cleaned_data.get("street") or ""
        details.house_number = self.cleaned_data.get("house_number") or ""
        details.postal_code = self.cleaned_data.get("postal_code") or ""
        details.hobbies = self.cleaned_data.get("hobbies") or ""
        details.date_of_birth = self.cleaned_data.get("date_of_birth")
        if commit:
            details.save()
        return user
