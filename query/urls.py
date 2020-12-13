from django.urls import path
from . import views


urlpatterns = [
    path('', views.QueryListView.as_view(), name='list'),
]
