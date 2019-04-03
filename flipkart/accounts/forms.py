from django import forms

class RegistrationForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name =forms.CharField(widget=forms.TextInput())
    email1 =forms.EmailField()
    password =forms.PasswordInput()
    contact =forms.CharField(widget=forms.TextInput())
    address =forms.CharField(widget=forms.TextInput())