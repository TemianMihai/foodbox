from django import forms
from .models import Formular

class FormularForm(forms.ModelForm):
    class Meta:
        model = Formular
        fields = ['name', 'phonenumber', 'email', 'gender',
                  'age', 'current_weight', 'desired_weight', 'height',
                  'name2', 'duration', 'restrictions', 'address']

    def clean_phonenumber(self):
        phonenumber = self.cleaned_data['phonenumber']
        if phonenumber[0] != '0' or phonenumber[1] != '7' or len(
                phonenumber) != 10 or phonenumber.isdigit() == False:
            raise forms.ValidationError("Invalid phonenumber")
        return phonenumber

    def clean_name(self):
        name = self.cleaned_data['name']
        if name.isdigit():
            raise forms.ValidationError("Name contains invalid characters")
        return name

    def clean_address(self):
        address = self.cleaned_data['address']
        return address

    def clean_email(self):
        email = self.cleaned_data['email']
        return email

    def clean_gender(self):
        gender = self.cleaned_data['gender']
        if gender.isdigit():
            raise forms.ValidationError("Gender contains invalid characters")
        return gender

    def clean_age(self):
        age = self.cleaned_data['age']
        if age.isdigit() == False:
            raise forms.ValidationError("Invalid age")
        return age

    def clean_current_weight(self):
        current_weight = self.cleaned_data['current_weight']
        if current_weight.isdigit() == False:
            raise forms.ValidationError("Invalid weight")
        return current_weight

    def clean_desired_weight(self):
        desired_weight = self.cleaned_data['desired_weight']
        if desired_weight.isdigit() == False:
            raise forms.ValidationError("Invalid weight")
        return desired_weight

    def clean_height(self):
        height = self.cleaned_data['height']
        if height.isdigit() == False:
            raise forms.ValidationError("Invalid height")
        return height

    def clean_name2(self):
        name2 = self.cleaned_data['name2']
        if name2.isdigit():
            raise forms.ValidationError("Last name contains invalid characters")
        return name2

    def clean_duration(self):
        duration = self.cleaned_data['duration']
        if duration.isdigit() == False:
            raise forms.ValidationError("Invalid duration of time")
        return duration

    def clean_restrictions(self):
        restrictions = self.cleaned_data['restrictions']
        return restrictions