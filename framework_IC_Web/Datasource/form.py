from django import forms;
from models import Datasource;

class DatasourceForm(forms.ModelForm):
    class Meta:
        model = Datasource;
