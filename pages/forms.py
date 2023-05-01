from django import forms

class PatientLoginForm(forms.Form):
    tcno = forms.CharField(max_length=11)
    password = forms.CharField(widget=forms.PasswordInput)