from django.contrib import admin
from .models import Query
from django.db.models import Count, Sum, Q, When, Case, IntegerField
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.functions import TruncDate, TruncDay, TruncMinute
import json


@admin.register(Query)
class QueryAdmin(admin.ModelAdmin):
    change_list_template = 'change_list.html'
    list_display = ("id", "url", "querytime", "ipaddress",
                    "exists", "timeout", "httpcode")
    ordering = ("-querytime",)

    def changelist_view(self, request, extra_context=None):

        # Data for connection errors: timed out connection or exists=True, i.e., unresolved name.
        chart_data1 = (
            Query.objects.annotate(date=TruncMinute("querytime")).values("date")
            .annotate(y=Sum(Case(When(timeout=True, then=1), When(timeout=False, then=0), output_field=IntegerField())
                            + Case(When(exists=False, then=1), When(exists=True, then=0), output_field=IntegerField())
                            )).order_by("-date")
        )
        as_json1 = json.dumps(list(chart_data1), cls=DjangoJSONEncoder)

        # Data for successful connections
        chart_data2 = (
            Query.objects.annotate(date=TruncMinute("querytime")).values("date").filter(Q(exists=True)).filter(Q(timeout=False))
            .annotate(y=Count("id")).order_by("-date")
        )
        as_json2 = json.dumps(list(chart_data2), cls=DjangoJSONEncoder)

        # Data for HTTP not OK
        chart_data3 = (
            Query.objects.filter(Q(exists=True)).filter(Q(timeout=False)).filter(~Q(httpcode="200")).annotate(date=TruncMinute("querytime")).values("date")
            .annotate(y=Count("id")).order_by("-date")
        )
        as_json3 = json.dumps(list(chart_data3), cls=DjangoJSONEncoder)

        # Data for HTTP OK
        chart_data4 = (
            Query.objects.filter(Q(exists=True)).filter(Q(timeout=False)).filter(Q(httpcode="200")).annotate(date=TruncMinute("querytime")).values("date")
            .annotate(y=Count("id")).order_by("-date")
        )
        as_json4 = json.dumps(list(chart_data4), cls=DjangoJSONEncoder)

        extra_context = extra_context or {"connection_errors": as_json1, "good_queries": as_json2, "status_not_ok": as_json3, "status_ok": as_json4}

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)
