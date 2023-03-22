
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status

from core.model.user import User
from core.model.viaje import Viaje
from core.model.maestro.subsistema import Subsistema
from core.model.maestro.sector import Sector
from core.model.maestro.zona import Zona
from core.model.maestro.bote import Bote
from core.model.maestro.especie import Especie
from core.model.maestro.unidad import Unidad
from core.model.trampa_historico import TrampaHistorico
from core.model.carnada_registro import CarnadaRegistro
from core.model.api_log import ApiLog

from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.permissions import IsAuthenticated

import json 

class ViajeView(APIView):
    #permission_classes = () #no requiere de permisos
    #serializer_class = TrampaHistoricoSerializer
    
    permission_classes = [HasAPIKey | IsAuthenticated] #requiere permisos

    def post(self, request):

        datos=request.data.get('datos')
        recorridos=[]
        
        objetos = []
        errores = []

        apilog=ApiLog()

        apilog.request_data=json.dumps(datos)
        apilog.save()

     

        i=0

        for dato in datos:
            i=i+1
            error=[]
            objeto = {"viaje":None,"trampa":[],"carnada_registro":[]}

            if Viaje.objects.filter(tripcode=dato['tripcode']).exists():
                error = error + ["[reg:"+str(i)+"] Ya existe un registro con tripcode {}".format(dato['tripcode'])]
                errores=errores+error
                continue

            subsistema = Subsistema.objects.filter(id=dato['mt_subsistema_id']).first()
            bote = Bote.objects.filter(id=dato['mt_bote_id']).first()
            especie = Especie.objects.filter(id=dato['mt_especie_id']).first()

            declaracion=None
            if dato['declaracion'] and len(str(dato['declaracion']).strip())>0 or str(dato['declaracion'])=="0":
                declaracion=dato['declaracion']

            n_trampas_agua=None
            if dato['n_trampas_agua'] and len(str(dato['n_trampas_agua']).strip())>0 or str(dato['n_trampas_agua'])=="0": 
                n_trampas_agua=dato['n_trampas_agua']

            n_trampas_visitadas=None
            if dato['n_trampas_visitadas'] and len(str(dato['n_trampas_visitadas']).strip())>0 or str(dato['n_trampas_visitadas'])=="0":
                n_trampas_visitadas=dato['n_trampas_visitadas']

            viaje = Viaje()
            viaje.tripcode = dato['tripcode']
            viaje.declaracion = dato['declaracion']
            viaje.mt_subsistema = subsistema
            viaje.mt_bote = bote
            viaje.fecha = dato['fecha']
            viaje.temporada = dato['temporada']
            viaje.n_trampas_agua = n_trampas_agua
            viaje.n_trampas_visitadas = n_trampas_visitadas
            viaje.mt_especie = especie
            total_capturado=None
            if len(str(dato['total_capturado']).replace(" ",""))>0:
                total_capturado=dato['total_capturado']
            viaje.total_capturado = total_capturado
            viaje.comentario = dato['comentario']
            viaje.es_web=False
            if dato['user_created']:
                viaje.user_created = User.objects.filter(id= dato['user_created']).first()
            if dato['user_updated']:
                viaje.user_updated = User.objects.filter(id= dato['user_updated']).first() 
            if dato['created_at']:
                viaje.local_creacion = dato['created_at']
            if dato['updated_at']:
                viaje.local_actualizacion = dato['updated_at']
            if dato['deleted_at']:
                viaje.deleted_at = dato['deleted_at']

            guardar=False
            if viaje.validar():
                error = error + viaje.validar(i)
            else:
                guardar=True
                objeto["viaje"]=viaje

            if dato['trampa_historico'] and len(dato['trampa_historico'])>0:
                
                for dato_trampa in dato['trampa_historico']:
                    
                    sector = None
                    if dato_trampa['mt_sector_id']:
                        sector = Sector.objects.filter(id=dato_trampa['mt_sector_id']).first()

                    zona = None
                    if dato_trampa['mt_sector_id']:
                        zona = Zona.objects.filter(id=dato_trampa['mt_zona_id']).first()

                    bycatch = None
                    if dato_trampa['bycatch_id']:
                        bycatch = Especie.objects.filter(id=dato_trampa['bycatch_id']).first()

              
                    trampa = TrampaHistorico()
                    trampa.viaje            =viaje
                    trampa.mt_sector        =sector
                    trampa.mt_zona          =zona
                    trampa.otro_sector      =dato_trampa['otro_sector']
                    trampa.ventana_escape   =dato_trampa['ventana_escape']
                    trampa.num_comercial    =dato_trampa['num_comercial']
                    trampa.num_no_comercial =dato_trampa['num_no_comercial']
                    trampa.bycatch          =bycatch
                    trampa.bycatch_cantidad =dato_trampa['bycatch_cantidad']
                    trampa.observaciones    =dato_trampa['observaciones']
                    if viaje.validar():
                        error = error + viaje.validar(i)
                    elif guardar:
                        objeto["trampa"].append(trampa)

            if dato['carnada_registro'] and len(dato['carnada_registro'])>0:
                
                for dato_carnada in dato['carnada_registro']:

                    unidad = None
                    if dato_carnada['mt_unidad_id']:
                        unidad = Unidad.objects.filter(id=dato_carnada['mt_unidad_id']).first()

                    carnada = None
                    if dato_carnada['mt_especie_id']:
                        carnada = Especie.objects.filter(id=dato_carnada['mt_especie_id']).first()

                    carnada_registro = CarnadaRegistro()
                    carnada_registro.viaje   = viaje
                    carnada_registro.mt_unidad  = unidad
                    carnada_registro.mt_especie = carnada
                    carnada_registro.volumen = dato_carnada['volumen']

                    if viaje.validar():
                        error = error + viaje.validar(i)
                    elif guardar:
                        objeto["carnada_registro"].append(carnada_registro)


            errores=errores+error

            if not error:
                objetos.append(objeto)
                recorridos.append(dato['id'])
            #viaje.save()
            #trampa.save()
            #carnada_registro.save()

            #recorridos.append(viaje.id)

        for objeto in objetos:
            if objeto["viaje"]:
                objeto["viaje"].save()
                #pass
                if objeto["trampa"]:
                    for trampa in objeto["trampa"]:
                        trampa.save()
                        #pass
                if objeto["carnada_registro"]:
                    for carnada_registro in objeto["carnada_registro"]:
                        carnada_registro.save()
                        #pass


        response={"save":recorridos,"errores":errores}
        apilog.response_data=json.dumps(response)
        apilog.save()

        return Response(response)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
