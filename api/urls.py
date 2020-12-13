from django.urls import path
from . import views


urlpatterns = [
    path('site_check', views.site_check, name='check'),
]
