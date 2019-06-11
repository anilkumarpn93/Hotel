from django import forms
from .models import login,user
class LoginForm(forms.ModelForm):
    class Meta:
        model = login
        fields = ['username','password']

class UserForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ['first_name','last_name','gender','dob','email','phone','place','login']
        widgets = {'login': forms.HiddenInput()}