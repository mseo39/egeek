from django import forms
from .models import Uploadfile

class uploadfile_form(forms.ModelForm):
    class Meta:
        model=Uploadfile
        fields=('title', 'file')