from django import forms


class UploadSheetForm(forms.Form):
    file = forms.FileField()
