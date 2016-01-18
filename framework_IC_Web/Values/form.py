from django import forms;
from models import Values;

class ValuesForm(forms.ModelForm):
    class Meta:
        model = Values;
