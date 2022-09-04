
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status

from core.model.maestro.arte import Arte
from core.model.maestro.arte import ArteSerializer

from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.permissions import IsAuthenticated

class ArteView(APIView):
    #permission_classes = () #no requiere de permisos
    serializer_class = ArteSerializer
    permission_classes = [HasAPIKey ] #requiere permisos

    def get_object(self, pk):
        try:
            return Arte.objects.get(id=pk)
        except Arte.DoesNotExist:
            return None

    def get(self, request,pk=None):
        if pk:
            data = self.get_object(pk)
            serializer = ArteSerializer(data, many=False)
        else:
            data = Arte.objects.all()
            serializer = ArteSerializer(data, many=True)  
        return Response(serializer.data)

      

    def put(self, request, pk=None):
        data = self.get_object(pk)
        if not data:
            raise Http404

        serializer = ArteSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):

        serializer = ArteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
