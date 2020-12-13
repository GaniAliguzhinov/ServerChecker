from django import forms
from sheets.models import Sheet


class UploadSheetForm(forms.ModelForm):
    class Meta:
        model = Sheet
        fields = ('sheet', )
