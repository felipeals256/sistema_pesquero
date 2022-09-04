
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status


from core.model.trampa import Trampa
from core.model.trampa import TrampaSerializer

"""
Trampa: No existe un identificador único de la trampa en el sistema. El que se utiliza es un
correlativo en la bitácora de viaje. Sólo se completa información de la trampa si ésta se ha visitado.
Si no hubo captura, se indica 0. La trampa pertenece a un Sector y a una zona.
"""

from core.model.maestro.sector import Sector
from core.model.maestro.zona import Zona

from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.permissions import IsAuthenticated

class TrampaView(APIView):
    #permission_classes = () #no requiere de permisos
    serializer_class = TrampaSerializer
    permission_classes = [HasAPIKey | IsAuthenticated] #requiere permisos

    def get_object(self, pk):
        try:
            return Trampa.objects.get(id=pk)
        except Trampa.DoesNotExist:
            return None

    def get(self, request,pk=None):
        if pk:
            data = self.get_object(pk)
            serializer = TrampaSerializer(data, many=False)
        else:
            data = Trampa.objects.all()
            serializer = TrampaSerializer(data, many=True)  
        return Response(serializer.data)

      

    def put(self, request, pk=None):
        data = self.get_object(pk)
        if not data:
            raise Http404

        serializer = TrampaSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):

        serializer = TrampaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
