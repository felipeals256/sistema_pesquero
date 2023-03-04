from django.db import models
from django.apps import apps
from core.env.base import Base
from rest_framework import serializers

from core.model.maestro.bote import Bote
from core.model.maestro.subsistema import Subsistema
from core.model.maestro.especie import Especie




"""
DESTINO: corresponde al destino que se le dará a la captura realizada en un viaje. La tabla
también manejará un histórico y su vigencia. Tiene un código destino, Tipo destino y un
nombre destino.

"""

class Viaje(Base):

    trampas_historicas=None;
    carnadas_registros=None;

    tripcode = models.CharField(
                                unique=True,
                                max_length=20
                            )
    

    declaracion = models.CharField(
                            null=True,
                            blank=True,
                            max_length=20
                            )

    mt_subsistema = models.ForeignKey(
                             Subsistema, 
                             on_delete=models.PROTECT,
                         )

    mt_bote = models.ForeignKey(
                             Bote, 
                             on_delete=models.PROTECT,
                         )

    fecha = models.DateField(
                            null=True,
                            blank=True,
                            )

    temporada = models.SmallIntegerField(
                            null=True,
                            blank=True,
                            )

    n_trampas_agua = models.SmallIntegerField(
                            null=True,
                            blank=True,
                            )

    n_trampas_visitadas = models.SmallIntegerField(
                            null=True,
                            blank=True,
                            )

    mt_especie = models.ForeignKey(
                             Especie, 
                             on_delete=models.PROTECT,
                         )

    comentario = models.CharField(
                            null=True,
                            blank=True,
                            max_length=200
                            )

    es_web = models.BooleanField(
                            null=True,
                            blank=True,)

    local_creacion = models.DateTimeField(
                                            blank=True,
                                            null=True,
                                            verbose_name="Fecha creación local"
                                            ) 
    local_actualizacion = models.DateTimeField(
                                            blank=True,
                                            null=True,
                                            verbose_name="Fecha modificación local"
                                            ) 

    total_capturado = models.FloatField(
                            null=True,
                            blank=True,
                            verbose_name="Total capturado"
                            )


    def getTrampaHistorico(self):
        if self.trampas_historicas == None:
            TrampaHistorico = apps.get_model('core', 'TrampaHistorico')
            self.trampas_historicas = TrampaHistorico.objects.filter(viaje_id=self.id)
            if not self.trampas_historicas:
                self.trampas_historicas=[]

        return self.trampas_historicas

    def getCarnadaRegistro(self):
        if self.carnadas_registros == None:
            CarnadaRegistro = apps.get_model('core', 'CarnadaRegistro')
            self.carnadas_registros = CarnadaRegistro.objects.filter(viaje_id=self.id)
            if not self.carnadas_registros:
                self.carnadas_registros=[]

        return self.carnadas_registros
        

    class Meta:
        verbose_name="Viaje"
        verbose_name_plural=verbose_name+"s"
        db_table =str(verbose_name).replace(' ','_').lower()
    
    def __str__(self):
        re = str(self.tripcode)
        return re


    def validar(self,i=None):
        error = []
        error = error + self.formatear_campos()


        reg=""
        if i:
            reg="[reg:"+str(i)+"] "

        if not self.tripcode:
            error.append(reg+"No es posible registrar un viaje sin tripcode")


        try:
            if not self.mt_subsistema:
                error.append(reg+"No es posible registrar un viaje sin subsistema.")
        except Exception as e:
            error.append(reg+"No es posible registrar un viaje sin subsistema.")

        try:
            if not self.mt_bote:
                error.append(reg+"No es posible registrar un viaje sin bote")
        except Exception as e:
            error.append(reg+"No es posible registrar un viaje sin bote")

        if not self.fecha:
            error.append(reg+"No es posible registrar un viaje sin fecha")

        return error

    def formatear_campos(self):
        error = []

        if self.tripcode or self.tripcode==0:
            self.tripcode=self.tripcode.strip()

        return error


class ViajeSerializer(serializers.ModelSerializer):

    trampa_historico = serializers.SerializerMethodField('getTrampaHistorico')
    carnada_registro = serializers.SerializerMethodField('getCarnadaRegistro')

    def getTrampaHistorico(self,model):
        from core.model.trampa_historico import TrampaHistoricoSerializer
        return TrampaHistoricoSerializer(model.getTrampaHistorico(),many=True).data

    def getCarnadaRegistro(self,model):
        from core.model.carnada_registro import CarnadaRegistroSerializer
        return CarnadaRegistroSerializer(model.getCarnadaRegistro(),many=True).data
    
    class Meta:
        model = Viaje
        fields='__all__'
        #fields = ('username', 'email')
        #extra_kwargs = {'password': {'write_only': True}}


