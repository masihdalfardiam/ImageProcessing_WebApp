from django import forms
from .models import UploadedData

class UploadedDataForm(forms.ModelForm):
    class Meta:
        model = UploadedData
        fields = ['text1', 'text2', 'text3', 'image']
