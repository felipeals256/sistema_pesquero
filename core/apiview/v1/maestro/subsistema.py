
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status

from core.model.maestro.subsistema import Subsistema
from core.model.maestro.subsistema import SubsistemaSerializer

class SubsistemaView(APIView):
    #permission_classes = () #no requiere de permisos
    serializer_class = SubsistemaSerializer
    

    def get_object(self, pk):
        try:
            return Subsistema.objects.get(id=pk)
        except Subsistema.DoesNotExist:
            return None

    def get(self, request,pk=None):
        if pk:
            data = self.get_object(pk)
            serializer = SubsistemaSerializer(data, many=False)
        else:
            data = Subsistema.objects.all()
            serializer = SubsistemaSerializer(data, many=True)  
        return Response(serializer.data)

      

    def put(self, request, pk=None):
        data = self.get_object(pk)
        if not data:
            raise Http404

        serializer = SubsistemaSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):

        serializer = SubsistemaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
