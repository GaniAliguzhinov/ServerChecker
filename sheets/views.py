from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UploadSheetForm
import xlrd


def upload_file(request):
    if request.method == 'POST':
        form = UploadSheetForm(request.POST, request.FILES)
        if form.is_valid():
            instance = UploadSheetForm(file=request.FILES['file'])
            instance.save()
            return HttpResponseRedirect(reverse('sheets.views.list'))
    else:
        form = UploadSheetForm()
    return render(request, 'upload.html', {'form': form})
