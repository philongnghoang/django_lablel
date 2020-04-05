from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username',max_length=30)
    email = forms.EmailField(label='Email')
    password1 =forms.CharField(label='Password',widget=forms.PasswordInput())
    password2 =forms.CharField(label='Password again',widget=forms.PasswordInput())
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError('Invalid Password')
    def clearn_username(self):
        username = self.clearn_data['username']
        if not re.search(r'^\w+$',username):
            raise forms.ValidationError('Invalid Username')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Username Exist')
    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'],
                    email=self.cleaned_data['email'],password=self.cleaned_data['password1'])
class ButtonClick(forms.Form):
    btn = forms.CharField()
class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)