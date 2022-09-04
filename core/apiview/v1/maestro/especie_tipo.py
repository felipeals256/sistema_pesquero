
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status

from core.model.maestro.especie_tipo import EspecieTipo
from core.model.maestro.especie_tipo import EspecieTipoSerializer

from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.permissions import IsAuthenticated
"""
Tipo Especie: agrupación de las especies, son tres tipos: crustáceos, moluscos, peces.
"""

class EspecieTipoView(APIView):
    #permission_classes = () #no requiere de permisos
    serializer_class = EspecieTipoSerializer
    permission_classes = [HasAPIKey | IsAuthenticated] #requiere permisos

    def get_object(self, pk):
        try:
            return EspecieTipo.objects.get(id=pk)
        except EspecieTipo.DoesNotExist:
            return None

    def get(self, request,pk=None):
        if pk:
            data = self.get_object(pk)
            serializer = EspecieTipoSerializer(data, many=False)
        else:
            data = EspecieTipo.objects.all()
            serializer = EspecieTipoSerializer(data, many=True)  
        return Response(serializer.data)

      

    def put(self, request, pk=None):
        data = self.get_object(pk)
        if not data:
            raise Http404

        serializer = EspecieTipoSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):

        serializer = EspecieTipoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
