from django.shortcuts import render,redirect
from django.views.generic import View

from django.contrib import messages

from core.model.viaje import Viaje
from core.model.viaje import ViajeSerializer

from core.model.maestro.bote import Bote
from core.model.maestro.especie import Especie
from core.model.maestro.especie import EspecieSerializer
from core.model.maestro.subsistema import Subsistema
from core.model.maestro.sector import Sector
from core.model.maestro.zona import Zona
from core.model.maestro.sector import SectorSerializer

from core.model.maestro.unidad import Unidad
from core.model.maestro.unidad import UnidadSerializer

from core.model.bote_vigencia import BoteVigencia

from core.model.trampa_historico import TrampaHistorico
from core.model.carnada_registro import CarnadaRegistro

from datetime import datetime

import json

class RegistroView(View):

	model = Viaje
	template_name="viaje/registro.html"
	success_message = "Registro Actualizado"



	def get(self,request,id=None,*args,**kwargs):

		viaje = Viaje.objects.filter(id=id).first()
		subsistemas = Subsistema.objects.all()
		sectores = Sector.objects.all()
		bote_vigencia = BoteVigencia.objects.filter( fecha_termino__gt = datetime.today() )
		especies = Especie.objects.filter(mt_especie_tipo__codigo=1)
		carnadas = Especie.objects.filter(mt_especie_tipo__codigo=2)
		bycatch = Especie.objects.filter(mt_especie_tipo__codigo=3)
		unidades = Unidad.objects.all()

		return render(request,self.template_name,{
			"viaje":ViajeSerializer(viaje,many=False).data,
			"subsistemas":subsistemas,
			"bote_vigencia":bote_vigencia,
			"especies":especies,
			"sectores":SectorSerializer(sectores,many=True).data,
			"bycatch":EspecieSerializer(bycatch,many=True).data,
			"carnadas":EspecieSerializer(carnadas,many=True).data,
			"unidades":UnidadSerializer(unidades,many=True).data,
			})



	def post(self,request,id=None,*args,**kwargs):
		viaje = Viaje.objects.filter(id=id).first()
		subsistemas = Subsistema.objects.all()
		sectores = Sector.objects.all()
		bote_vigencia = BoteVigencia.objects.filter( fecha_termino__gt = datetime.today() )
		especies = Especie.objects.filter(mt_especie_tipo__codigo=1)
		carnadas = Especie.objects.filter(mt_especie_tipo__codigo=2)
		bycatch = Especie.objects.filter(mt_especie_tipo__codigo=3)
		unidades = Unidad.objects.all()

		valores={
			"viaje":ViajeSerializer(viaje,many=False).data,
			"subsistemas":subsistemas,
			"bote_vigencia":bote_vigencia,
			"especies":especies,
			"sectores":SectorSerializer(sectores,many=True).data,
			"bycatch":EspecieSerializer(bycatch,many=True).data,
			"carnadas":EspecieSerializer(carnadas,many=True).data,
			"unidades":UnidadSerializer(unidades,many=True).data,
		}


		error = ""

		try:
			dato = request.POST.get('viaje_send')
			dato = json.loads(dato)
		except Exception as e:
			error="No pudimos procesar el formulario"
			messages.error(self.request, error.upper())
			return render(request,self.template_name,valores)
		

		fecha  = dato['fecha'].replace(" ","").split("-")
		dia=fecha[2]
		mes=fecha[1]
		anio=fecha[0]
		if len(fecha[2]) == 4:
			dia=fecha[2]
			mes=fecha[1]
			anio=fecha[0]

		subsistema = Subsistema.objects.filter(id=dato['mt_subsistema_id']).first()
		if not subsistema:
			error="Ingrese el Subsistema"
			messages.error(self.request, error.upper())
			return render(request,self.template_name,valores)

		bote = Bote.objects.filter(id=dato['mt_bote_id']).first()
		if not bote:
			error="Ingrese el Bote"
			messages.error(self.request, error.upper())
			return render(request,self.template_name,valores)

		especie = Especie.objects.filter(id=dato['mt_especie_id']).first()
		if not especie:
			error="Ingrese una Especie"
			messages.error(self.request, error.upper())
			return render(request,self.template_name,valores)



		_viaje = Viaje.objects.filter(id=dato['id']).first()
		_viaje.tripcode=str(subsistema.codigo).strip()+str(bote.matricula).strip()+"_"+str(dia)+str(mes)+str(anio)
		
		if Viaje.objects.filter(tripcode=_viaje.tripcode).exclude(id=_viaje.id).exists():
			error="Ya existe un registro con este tripcode"
			messages.error(self.request, error.upper())
			return render(request,self.template_name,valores)

		n_trampas_agua=None
		if dato['n_trampas_agua'] and len(str(dato['n_trampas_agua']).strip())>0 or str(dato['n_trampas_agua'])=="0": 
			n_trampas_agua=dato['n_trampas_agua']

		n_trampas_visitadas=None
		if dato['n_trampas_visitadas'] and len(str(dato['n_trampas_visitadas']).strip())>0 or str(dato['n_trampas_visitadas'])=="0":
			n_trampas_visitadas=dato['n_trampas_visitadas']

		#viaje.tripcode = dato['tripcode']
		_viaje.declaracion = dato['declaracion']
		_viaje.mt_subsistema = subsistema
		_viaje.mt_bote = bote
		_viaje.fecha = dato['fecha']
		_viaje.temporada = dato['temporada']
		_viaje.n_trampas_agua = n_trampas_agua
		_viaje.n_trampas_visitadas = n_trampas_visitadas
		_viaje.mt_especie = especie
		total_capturado=None
		if len(str(dato['total_capturado']).replace(" ",""))>0:
			total_capturado=dato['total_capturado']
		_viaje.total_capturado = total_capturado
		_viaje.comentario = dato['comentario']
		
		list_trampas_historicas=dato['list_trampas_historicas']
		list_carnadas=dato['list_carnadas']




		trampas_reg=[]
		if dato['list_trampas_historicas'] and len(dato['list_trampas_historicas'])>0:
			for dato_trampa in dato['list_trampas_historicas']:
				sector = None
				if dato_trampa['mt_sector_id']:
					sector = Sector.objects.filter(id=dato_trampa['mt_sector_id']).first()

				zona = None
				if dato_trampa['mt_zona_id']:
					zona = Zona.objects.filter(id=dato_trampa['mt_zona_id']).first()

				_bycatch = None
				if dato_trampa['bycatch_id']:
					_bycatch = Especie.objects.filter(id=dato_trampa['bycatch_id']).first()

				trampa = TrampaHistorico()
				trampa.viaje            =_viaje
				trampa.mt_sector        =sector
				trampa.mt_zona          =zona
				trampa.otro_sector      =dato_trampa['otro_sector']
				trampa.ventana_escape   =dato_trampa['ventana_escape']
				trampa.num_comercial    =dato_trampa['num_comercial']
				trampa.num_no_comercial =dato_trampa['num_no_comercial']
				trampa.bycatch          =_bycatch
				trampa.bycatch_cantidad =dato_trampa['bycatch_cantidad']
				trampa.observaciones    =dato_trampa['observaciones']
				if viaje.validar():
					error=viaje.validar(i)
					messages.error(self.request, error)
					return render(request,self.template_name,valores)
				
				trampas_reg.append(trampa)

		carnadas_reg=[]
		if dato['list_carnadas'] and len(dato['list_carnadas'])>0:
                
			for dato_carnada in dato['list_carnadas']:
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

				if carnada_registro.validar():
					error=viaje.validar(i)
					messages.error(self.request, error)
					return render(request,self.template_name,valores)
            
				carnadas_reg.append(carnada_registro)








		for reg in TrampaHistorico.objects.filter(viaje_id=_viaje.id):
			reg.delete(request)
		for reg in CarnadaRegistro.objects.filter(viaje_id=_viaje.id):
			reg.delete(request)


		_viaje.save(request)

		for reg in trampas_reg:
			reg.save(request)

		for reg in carnadas_reg:
			reg.save(request)

		


		messages.success(self.request, self.success_message.upper())
		#messages.error(self.request, "error")

		

		return render(request,self.template_name,{
			"viaje":ViajeSerializer(_viaje,many=False).data,
			"subsistemas":subsistemas,
			"bote_vigencia":bote_vigencia,
			"especies":especies,
			"sectores":SectorSerializer(sectores,many=True).data,
			"bycatch":EspecieSerializer(bycatch,many=True).data,
			"carnadas":EspecieSerializer(carnadas,many=True).data,
			"unidades":UnidadSerializer(unidades,many=True).data,
		})


