from django import forms;
from models import Radio, RadioInfo;

class RadioForm(forms.ModelForm):
    class Meta:
        model = Radio;

class RadioInfoForm(forms.ModelForm):
    class Meta:
        model = RadioInfo;
