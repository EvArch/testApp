from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Enter username',max_length=50)
    password = forms.CharField(label='Enter password',max_length=50)
    email = forms.CharField(label='Enter email',max_length=50)
