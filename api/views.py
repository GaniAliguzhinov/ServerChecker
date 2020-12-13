from django.shortcuts import render
from query.models import Query
from query.serializers import QuerySerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def site_check(request):
    if request.method == 'GET':
        url = request.GET.get('url', None)
        if url is not None:
            query = Query(url=url)
            serializer = QuerySerializer(query)
            return Response(serializer.data)
        else:
            return Response()

