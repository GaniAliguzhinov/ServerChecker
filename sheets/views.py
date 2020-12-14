from django.shortcuts import render, redirect
from .forms import UploadSheetForm
import openpyxl
from io import BytesIO
from sheets.tasks import process


def upload_file(request):
    """
    View for uploading an excel file with urls.
    Once uploaded, the file will be processed asynchronously.
    """
    if request.method == 'POST':
        form = UploadSheetForm(request.POST, request.FILES)
        if form.is_valid():
            process_sheet(request.FILES['sheet'])
            return redirect('/queries/')
    else:
        form = UploadSheetForm()
    return render(request, 'upload.html', {'form': form})


def process_sheet(file):
    """
    Iterate over the excel file and process each url
    """
    wb = openpyxl.load_workbook(filename=BytesIO(file.read()))
    sheet = wb.active

    # To speed up, use a Pool
    urls = []

    for row in range(1, sheet.max_row+1):
        url = sheet.cell(row=row, column=1).value
        if'.' not in url:
            continue
        urls.append(url)

    # Process queries on all urls
    process.delay(urls)
