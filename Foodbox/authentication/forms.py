from django import forms
from django.contrib.auth.models import User
from .models import Account


class LoginForm(forms.Form):
    username = forms.CharField(max_length = 30, label='Username',
                            widget = forms.TextInput(attrs={
                                'required':'required',
                                'placeholder':'Username'
                            }))
    password = forms.CharField(max_length = 30, label = "Password",
                               widget = forms.PasswordInput(attrs={
                                   'required':'required',
                                   'placeholder':'Password'
                               }))

class UserRegisterForm(forms.ModelForm):

    retypepassword = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Retype password',
        'label': 'Retype password',
        'required': 'required'}))

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'retypepassword']
        widgets = {
            'username': forms.TextInput({'required': 'required',
                                         'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'required': 'required',
                                                   'placeholder': 'Password',
                                                   'type': 'password'}),
            'first_name': forms.TextInput({'required': 'required',
                                         'placeholder': 'First Name'}),
            'last_name': forms.TextInput({'required': 'required',
                                         'placeholder': 'Last Name'}),
            'retypepassword': forms.PasswordInput(attrs={'required':'required',
                                                         'placeholder':'Retype password',
                                                         'type':'password'}),
        }

    def clean_username(self):
        user_name = self.cleaned_data['username']
        if User.objects.filter(username=user_name).count():
            raise forms.ValidationError("This email already exists")
        return user_name

    def clean_retypepassword(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['retypepassword']
        if password.isdigit():
            raise forms.ValidationError("Password is entirely numeric")
        if password != password2:
            raise forms.ValidationError("Passwords do not match")
        if len(password) < 8:
            raise forms.ValidationError("Password is too short")
        return password2


    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if (
                not (first_name.isalnum() or first_name.isalpha())
        ):
            raise forms.ValidationError("Name contains invalid characters")
        return first_name


    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if (
                not (last_name.isalnum() or last_name.isalpha())
        ):
            raise forms.ValidationError("Name contains invalid characters")
        return last_name

class AccRegisterForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['phonenumber']
        widgets = {
            'phonenumber' : forms.TextInput({'required':'required','placeholder':'Phonenumber'})
        }
    def clean_phonenumber(self):
        phone_number = self.cleaned_data['phonenumber']
        if phone_number[0] != '0' or phone_number[1] != '7' or len(phone_number) != 10 or phone_number.isdigit() == False:
            raise forms.ValidationError("Invalid phonenumber")
        return phone_number
