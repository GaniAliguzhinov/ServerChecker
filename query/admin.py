from django.contrib import admin
from .models import Query


@admin.register(Query)
class QueryAdmin(admin.ModelAdmin):
    pass
