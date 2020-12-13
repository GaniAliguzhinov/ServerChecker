from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Query


class QueryListView(ListView):
    model = Query
