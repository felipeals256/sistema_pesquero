
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status

from core.model.maestro.bote import Bote
from core.model.maestro.bote import BoteSerializer

from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.permissions import IsAuthenticated

class SubsistemaBoteView(APIView):
    #permission_classes = () #no requiere de permisos
    serializer_class = BoteSerializer
    #permission_classes = [HasAPIKey | IsAuthenticated] #requiere permisos
    
    def post(self, request, parametro=None,pk=None):

        data = []

    

        data = Bote.objects.raw("""

            SELECT mb.* from bote_vigencia bv 
            left join mt_bote mb on mb.id = bv.mt_bote_id 
            where ( bv.fecha_termino < now() or bv.fecha_termino is null )
            and bv.mt_subsistema_id  = {pk}
            """.format(pk=pk))



        serializer = BoteSerializer(data, many=True)  

        return Response(serializer.data)
    
