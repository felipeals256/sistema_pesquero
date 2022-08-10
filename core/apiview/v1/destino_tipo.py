
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status

from core.model.destino_tipo import DestinoTipo
from core.model.destino_tipo import DestinoTipoSerializer

class DestinoTipoView(APIView):
    #permission_classes = () #no requiere de permisos
    serializer_class = DestinoTipoSerializer
    

    def get_object(self, pk):
        try:
            return DestinoTipo.objects.get(id=pk)
        except DestinoTipo.DoesNotExist:
            return None

    def get(self, request,pk=None):
        if pk:
            data = self.get_object(pk)
            serializer = DestinoTipoSerializer(data, many=False)
        else:
            data = DestinoTipo.objects.all()
            serializer = DestinoTipoSerializer(data, many=True)  
        return Response(serializer.data)

      

    def put(self, request, pk=None):
        data = self.get_object(pk)
        if not data:
            raise Http404

        serializer = DestinoTipoSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):

        serializer = DestinoTipoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
