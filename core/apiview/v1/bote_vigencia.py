
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status

from core.model.bote_vigencia import BoteVigencia
from core.model.bote_vigencia import BoteVigenciaSerializer

"""
un bote puede es en más de una isla, pero tienen vijencia, se debe listar un bote en una isla cuando tenga vigencia
"""
class BoteVigenciaView(APIView):
    #permission_classes = () #no requiere de permisos
    serializer_class = BoteVigenciaSerializer
    

    def get_object(self, pk):
        try:
            return BoteVigencia.objects.get(id=pk)
        except BoteVigencia.DoesNotExist:
            return None

    def get(self, request,pk=None):
        if pk:
            data = self.get_object(pk)
            serializer = BoteVigenciaSerializer(data, many=False)
        else:
            data = BoteVigencia.objects.all()
            serializer = BoteVigenciaSerializer(data, many=True)  
        return Response(serializer.data)

      

    def put(self, request, pk=None):
        data = self.get_object(pk)
        if not data:
            raise Http404

        serializer = BoteVigenciaSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):

        serializer = BoteVigenciaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
