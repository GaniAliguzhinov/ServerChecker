from rest_framework import serializers
from query.models import Query


class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = ['url', 'exists', 'timeout', 'ipaddress', 'httpcode',
                  'querytime']

