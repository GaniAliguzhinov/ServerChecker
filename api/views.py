from query.models import Query
from query.serializers import QuerySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def site_check(request):
    if request.method == 'GET':
        url = request.GET.get('url', None)
        if url is not None:
            try:
                query = Query(url=url)
                query.save()
                serializer = QuerySerializer(query)
            except Exception:
                return Response()
            return Response(serializer.data)
        else:
            return Response()
