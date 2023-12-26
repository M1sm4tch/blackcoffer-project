from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
import json
from reports.models import DataModel
from .serializers import DataModelSerializer
from rest_framework import status
from rest_framework.views import APIView

class BulkDataModelCreateView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = DataModelSerializer(data=data, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getData(request):
    data = DataModel.objects.all()
    print(data)
    serializer = DataModelSerializer(data, many=True)
    print(serializer.data)
    return Response(serializer.data)

@api_view(['POST'])
def postdata(request):
    serializer = DataModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)