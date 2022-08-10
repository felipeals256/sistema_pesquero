
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status

from core.model.destino import Destino
from core.model.destino import DestinoSerializer
"""
DESTINO: corresponde al destino que se le dará a la captura realizada en un viaje. La tabla
también manejará un histórico y su vigencia. Tiene un código destino, Tipo destino y un
nombre destino.

"""

class DestinoView(APIView):
    #permission_classes = () #no requiere de permisos
    serializer_class = DestinoSerializer
    

    def get_object(self, pk):
        try:
            return Destino.objects.get(id=pk)
        except Destino.DoesNotExist:
            return None

    def get(self, request,pk=None):
        if pk:
            data = self.get_object(pk)
            serializer = DestinoSerializer(data, many=False)
        else:
            data = Destino.objects.all()
            serializer = DestinoSerializer(data, many=True)  
        return Response(serializer.data)

      

    def put(self, request, pk=None):
        data = self.get_object(pk)
        if not data:
            raise Http404

        serializer = DestinoSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):

        serializer = DestinoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
