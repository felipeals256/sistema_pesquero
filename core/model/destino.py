from django.db import models


from rest_framework import serializers

from core.model.destino_tipo import DestinoTipo

"""
DESTINO: corresponde al destino que se le dará a la captura realizada en un viaje. La tabla
también manejará un histórico y su vigencia. Tiene un código destino, Tipo destino y un
nombre destino.

"""

class Destino(models.Model):


    codigo = models.IntegerField(
                            unique=True,
                            )

    nombre = models.CharField(max_length=255,
                            null=True,
                            blank=True,
                            )

    descripcion = models.CharField(max_length=255,
                            null=True,
                            blank=True,
                            )

    vigencia = models.DateField(
                            null=True,
                            blank=True,
                            )

    destino_tipo = models.ForeignKey(
                             DestinoTipo, 
                             on_delete=models.PROTECT,
                         )


        

    class Meta:
        verbose_name="Destino"
        verbose_name_plural=verbose_name+"s"
        db_table =str(verbose_name).replace(' ','_').lower()
    
    def __str__(self):
        re = str(self.codigo)
        return re



class DestinoSerializer(serializers.ModelSerializer):

    #rut = serializers.SerializerMethodField('getRut')

    
    class Meta:
        model = Destino
        fields='__all__'
        #fields = ('username', 'email')
        #extra_kwargs = {'password': {'write_only': True}}


