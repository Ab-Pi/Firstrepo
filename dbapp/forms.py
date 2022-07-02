from dataclasses import fields
from stat import FILE_ATTRIBUTE_NORMAL
from xml.parsers.expat import model
from django import forms
from django.apps import apps

from dbapp.models import appointment, doctor, patient,complain

class loginform(forms.Form):
    username = forms.CharField(max_length=30,required=True)
    password = forms.CharField(max_length=30,required=True, widget=forms.PasswordInput)

class ins_doctorform(forms.ModelForm):
    class Meta:
        model = doctor
        fields = '__all__'

class ins_patientform(forms.ModelForm):
    class Meta:
        model = patient
        fields = '__all__'

class ins_appointform(forms.ModelForm):
    class Meta:
        model = appointment
        fields = '__all__'

class ins_complainform(forms.ModelForm):
    class Meta:
        model = complain
        fields = '__all__'



