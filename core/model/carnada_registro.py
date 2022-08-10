from django.db import models


from rest_framework import serializers

from core.model.maestro.unidad import Unidad
from core.model.maestro.unidad import UnidadSerializer
from core.model.maestro.especie import Especie
from core.model.maestro.especie import EspecieSerializer
from core.model.viaje import Viaje



from core.env.base import Base
class CarnadaRegistro(Base):

    #es el tripcode del viaje

    viaje = models.ForeignKey(
                            Viaje, 
                            on_delete=models.PROTECT,
                         )


    #Unidades: Formato lista desplegable de dos valores: p (peso) n(número) que indica si el
    mt_unidad = models.ForeignKey(
                            Unidad, 
                            on_delete=models.PROTECT,
                            null=True,
                            blank=True,

                         )

    mt_especie = models.ForeignKey(
                            Especie, 
                            on_delete=models.PROTECT,
                            null=True,
                            blank=True,
                         )

    volumen = models.IntegerField(
                            null=True,
                            blank=True,
                            )

    


    def validar(self,i=None):
        error = []
        error = error + self.formatear_campos()


        return error

    def formatear_campos(self):
        error = []



        return error
        

    class Meta:
        verbose_name="Carnada Registro"
        verbose_name_plural=verbose_name+"s"
        db_table =(str(verbose_name).replace(' ','_')).lower()
    
    def __str__(self):
        re = str(self.codigo)
        return re



class CarnadaRegistroSerializer(serializers.ModelSerializer):

    obj_especie = serializers.SerializerMethodField('getEspecie')
    obj_sector = serializers.SerializerMethodField('getUnidad')

    def getEspecie(self,model):
        return EspecieSerializer(model.mt_especie,many=False).data

    def getUnidad(self,model):
        return UnidadSerializer(model.mt_unidad,many=False).data

    
    class Meta:
        model = CarnadaRegistro
        fields='__all__'
        #fields = ('username', 'email')
        #extra_kwargs = {'password': {'write_only': True}}


