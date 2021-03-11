from django import forms 
from .models import SignUp,LogIn
from django.db import models

from django import forms 



class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = SignUp
        fields= '__all__'

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Password does not match")

        # return cleaned_data

class LogInForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = LogIn
        fields = '__all__'


