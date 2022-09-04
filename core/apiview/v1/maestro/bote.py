
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status

from core.model.maestro.bote import Bote
from core.model.maestro.bote import BoteSerializer

from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.permissions import IsAuthenticated
"""
BOTE: Se administrará un histórico del bote, con sus características actualizadas desde el
archivo CTM al comienzo de la temporada. Si se modifica alguna característica, se crea un
nuevo registro y al anterior se le ingresa Fecha término registro. Todos los registros de la tabla
BOTE que no tengan fecha término registro estarán vigentes. Sólo puede existir un registro
vigente por matrícula. Para dar de baja un BOTE se ingresa la Fecha término registro. Se
registra la información del id usuario que realiza acciones sobre esta tabla.
"""
class BoteView(APIView):
    #permission_classes = () #no requiere de permisos
    serializer_class = BoteSerializer
    permission_classes = [HasAPIKey | IsAuthenticated] #requiere permisos

    def get_object(self, pk):
        try:
            return Bote.objects.get(id=pk)
        except Bote.DoesNotExist:
            return None

    def get(self, request,pk=None):
        if pk:
            data = self.get_object(pk)
            serializer = BoteSerializer(data, many=False)
        else:
            data = Bote.objects.all()
            serializer = BoteSerializer(data, many=True)  
        return Response(serializer.data)

      

    def put(self, request, pk=None):
        data = self.get_object(pk)
        if not data:
            raise Http404

        serializer = BoteSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):

        serializer = BoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
