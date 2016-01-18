from django import forms;
from models import Tag, TagInfo;

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag

class TagInfoForm(forms.ModelForm):
    class Meta:
        model = TagInfo
