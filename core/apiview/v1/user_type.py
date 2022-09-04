
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status

from core.model.user_type import UserType
from core.model.user_type import UserTypeSerializer

"""
un bote puede es en más de una isla, pero tienen vijencia, se debe listar un bote en una isla cuando tenga vigencia
"""

from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.permissions import IsAuthenticated

class UserTypeView(APIView):
    #permission_classes = () #no requiere de permisos
    serializer_class = UserTypeSerializer
    permission_classes = [HasAPIKey | IsAuthenticated] #requiere permisos

    def get_object(self, pk):
        try:
            return UserType.objects.get(id=pk)
        except UserType.DoesNotExist:
            return None

    def get(self, request,pk=None):
        if pk:
            data = self.get_object(pk)
            serializer = UserTypeSerializer(data, many=False)
        else:
            data = UserType.objects.all()
            serializer = UserTypeSerializer(data, many=True)  
        return Response(serializer.data)

      

    def put(self, request, pk=None):
        data = self.get_object(pk)
        if not data:
            raise Http404

        serializer = UserTypeSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):

        serializer = UserTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
