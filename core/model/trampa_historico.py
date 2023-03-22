from django.db import models


from rest_framework import serializers
from core.env.base import Base

"""
Trampa: No existe un identificador único de la trampa en el sistema. El que se utiliza es un
correlativo en la bitácora de viaje. Sólo se completa información de la trampa si ésta se ha visitado.
Si no hubo captura, se indica 0. La trampa pertenece a un Sector y a una zona.
"""

from core.model.maestro.sector import Sector
from core.model.maestro.zona import Zona, ZonaSerializer
from core.model.maestro.sector import SectorSerializer
from core.model.viaje import Viaje
from core.model.maestro.especie import Especie
from core.model.maestro.especie import EspecieSerializer

class TrampaHistorico(Base):

    """
    Identificador de la trampa(*): Número de dos dígitos. Correlativo automático en este
    formulario.
    """

    viaje  = models.ForeignKey(
                             Viaje, 
                             on_delete=models.PROTECT,
                            )
    
    

    mt_sector  = models.ForeignKey(
                            Sector, 
                            null=True,
                            blank=True,
                            on_delete=models.PROTECT,
                            )

    otro_sector = models.CharField(
                            null=True,
                            blank=True,
                            max_length=100,
                            )

    ventana_escape = models.BooleanField(
                            null=True,
                            blank=True,
                            )

    """
        Número Com(*) Formato número entero de dos dígitos. Cantidad de la Especie encontrada en
        la trampa que es de tamaño Comercial. Validar que no sea mayor a 50 ni menor que 0.
    """
    num_comercial = models.SmallIntegerField(
                            null=True,
                            blank=True,
                            )

    """
    Número NoCom: Formato número entero de dos dígitos. Cantidad de la Especie encontrada en
    la trampa que no es de tamaño Comercial. Validar que no sea mayor a 100 ni menor a 0 (OJO:
    0 es distinto a vacío). Si no ingresa nada, poner en la base de datos NA.
    """
    num_no_comercial = models.SmallIntegerField(
                            null=True,
                            blank=True,
                            )


    #Bycatch: captura ocasional, aquí lista desplegable sin cangrejo ni langosta (dep de lo que estás registrando) (hasta tres especies)
    bycatch = models.ForeignKey(
                            Especie, 
                            on_delete=models.PROTECT,
                            null=True,
                            blank=True,
                         )

    bycatch_cantidad = models.IntegerField(
                            null=True,
                            blank=True,
                            )

    observaciones = models.CharField(max_length=100,
                            null=True,
                            blank=True,
                            )

    mt_zona  = models.ForeignKey(
                            Zona, 
                            null=True,
                            blank=True,
                            on_delete=models.PROTECT,
                            )


    """
        Si se trata de la isla Alejandro Selkirk sólo langosta, habilitar el ingreso para los campos:
        Marca:
        Talla:
    """
    """
    marca = models.CharField(max_length=100,
                            null=True,
                            blank=True,
                            )
    talla = models.CharField(max_length=100,
                            null=True,
                            blank=True,
                            )
    """





    def validar(self,i=None):
        error = []
        error = error + self.formatear_campos()


        return error

    def formatear_campos(self):
        error = []

        if self.observaciones or self.observaciones==0:
            self.observaciones=self.observaciones.strip()

        return error


        

    class Meta:
        verbose_name="Trampa Historico"
        verbose_name_plural=verbose_name+"s"
        db_table =str(verbose_name).replace(' ','_').lower()
    
    def __str__(self):
        return str(self.codigo)
        



class TrampaHistoricoSerializer(serializers.ModelSerializer):

    obj_especie = serializers.SerializerMethodField('get_especie')
    obj_sector = serializers.SerializerMethodField('get_sector')
    obj_zona = serializers.SerializerMethodField('get_zona')

    def get_especie(self,model):
        return EspecieSerializer(model.bycatch,many=False).data

    def get_sector(self,model):
        return SectorSerializer(model.mt_sector,many=False).data

    def get_zona(self,model):
        return ZonaSerializer(model.mt_zona,many=False).data

    
    class Meta:
        model = TrampaHistorico
        fields='__all__'
        #fields = ('username', 'email')
        #extra_kwargs = {'password': {'write_only': True}}


