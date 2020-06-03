from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from clinic.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=250, help_text='Add a valid email address.')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login!")

class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email', 'username')

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = User.objects.exclude(pk=self.instance.pk).get(email=email)
            except User.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is already in use!' % account.email)

    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                account = User.objects.exclude(pk=self.instance.pk).get(username=username)
            except User.DoesNotExist:
                return username
            raise forms.ValidationError('Username "%s" is already in use!' % account.username)
