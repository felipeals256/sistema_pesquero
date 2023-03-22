
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status

from core.model.maestro.sector import Sector
from core.model.maestro.sector import SectorSerializer

from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.permissions import IsAuthenticated
from django.forms.models import model_to_dict

class SectorByView(APIView):
    #permission_classes = () #no requiere de permisos
    serializer_class = SectorSerializer
    #permission_classes = [HasAPIKey | IsAuthenticated] #requiere permisos
    
    def post(self, request, parametro=None,pk=None):

        data = []

        if str(parametro).lower().replace(" ","")=='subsistema':
            resultado = []
            data = Sector.objects.raw("""

                SELECT  mt_sector.*, mt_zona.id as mt_zona_id , mt_zona.descripcion as mt_zona_descripcion
                FROM mt_sector
                left join mt_zona_mt_sector on mt_zona_mt_sector.sector_id = mt_sector.id 
                left join mt_subsistema_mt_zona on mt_subsistema_mt_zona.zona_id = mt_zona_mt_sector.zona_id 
                left join mt_zona on mt_subsistema_mt_zona.zona_id = mt_zona.id 
                where mt_subsistema_mt_zona.subsistema_id = {pk}
                """.format(pk=pk))

            for obj in data:
                _obj=model_to_dict(obj)
                _obj['mt_zona_id']=obj.mt_zona_id
                _obj['mt_zona_descripcion']=obj.mt_zona_descripcion
                resultado.append(_obj)
            return Response(resultado)

        else:
            data = Sector.objects.all()

        serializer = SectorSerializer(data, many=True)  

        return Response(serializer.data)
    
