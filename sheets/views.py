from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UploadSheetForm
from openpyxl import Workbook
import openpyxl
from io import BytesIO
from query.models import Query
from multiprocessing import Process, Queue, Pool, cpu_count


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


def process_query(url):
    query = Query(url=url)
    query.save()


def process_sheet(file):
    """
    Iterate over the excel file and process each url
    """
    wb = openpyxl.load_workbook(filename=BytesIO(file.read()))
    sheet = wb.active

    # To speed up, use a Pool
    pool = Pool(cpu_count())
    urls = []

    for row in range(1, sheet.max_row+1):
        url = sheet.cell(row=row, column=1).value
        if'.' not in url:
            continue
        urls.append(url)

    # Process queries on all urls
    pool.map(process_query, urls)
