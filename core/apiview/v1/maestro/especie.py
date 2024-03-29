
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status


from core.model.maestro.especie import Especie
from core.model.maestro.especie import EspecieSerializer
"""
Especie: Formato lista desplegable con dos campos: LANGOSTA; CANGREJO. Por defecto debe
estar LANGOSTA.
"""

from core.model.maestro.especie_tipo import EspecieTipo

class EspecieView(APIView):
    #permission_classes = () #no requiere de permisos
    serializer_class = EspecieSerializer
    

    def get_object(self, pk):
        try:
            return Especie.objects.get(id=pk)
        except Especie.DoesNotExist:
            return None

    def get(self, request,pk=None):
        if pk:
            data = self.get_object(pk)
            serializer = EspecieSerializer(data, many=False)
        else:
            data = Especie.objects.all()
            serializer = EspecieSerializer(data, many=True)  
        return Response(serializer.data)

      

    def put(self, request, pk=None):
        data = self.get_object(pk)
        if not data:
            raise Http404

        serializer = EspecieSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):

        serializer = EspecieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
