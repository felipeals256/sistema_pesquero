
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status

from core.model.maestro.sector import Sector
from core.model.maestro.sector import SectorSerializer

class SectorView(APIView):
    #permission_classes = () #no requiere de permisos
    serializer_class = SectorSerializer
    

    def get_object(self, pk):
        try:
            return Sector.objects.get(id=pk)
        except Sector.DoesNotExist:
            return None

    def get(self, request,pk=None):
        if pk:
            data = self.get_object(pk)
            serializer = SectorSerializer(data, many=False)
        else:
            data = Sector.objects.all()
            serializer = SectorSerializer(data, many=True)  
        return Response(serializer.data)

      

    def put(self, request, pk=None):
        data = self.get_object(pk)
        if not data:
            raise Http404

        serializer = SectorSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):

        serializer = SectorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
