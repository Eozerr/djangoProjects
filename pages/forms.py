from django import forms
from .models import Bolum,Doktor, Hasta,Randevu
from django.db.models import QuerySet as queryset


class LoginForm(forms.Form):
    tc_no = forms.CharField(label='tcno', max_length=11)
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    
    
class RandevuForm(forms.ModelForm):
    hastatcno = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        tcno = kwargs.pop('tcno', None)
        super(RandevuForm, self).__init__(*args, **kwargs)
        self.fields['hastatcno'].initial = tcno

    class Meta:
        model = Randevu
        fields = [ 'tarih', 'saat', 'bolum','hastatcno']
        widgets = {
            'tarih': forms.DateInput(attrs={'type': 'date'}),
            'saat': forms.TimeInput(attrs={'type': 'time'}),
            'bolum': forms.Select(attrs={'id': 'bolum-secimi'})
        }


