
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status

from core.model.carnada import Carnada
from core.model.carnada import CarnadaSerializer

class CarnadaView(APIView):
    #permission_classes = () #no requiere de permisos
    serializer_class = CarnadaSerializer
    

    def get_object(self, pk):
        try:
            return Carnada.objects.get(id=pk)
        except Carnada.DoesNotExist:
            return None

    def get(self, request,pk=None):
        if pk:
            data = self.get_object(pk)
            serializer = CarnadaSerializer(data, many=False)
        else:
            data = Carnada.objects.all()
            serializer = CarnadaSerializer(data, many=True)  
        return Response(serializer.data)

      

    def put(self, request, pk=None):
        data = self.get_object(pk)
        if not data:
            raise Http404

        serializer = CarnadaSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):

        serializer = CarnadaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
