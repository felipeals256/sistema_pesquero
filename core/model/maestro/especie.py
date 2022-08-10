from django.db import models


from rest_framework import serializers

from core.model.maestro.unidad import Unidad

"""
Especie: Formato lista desplegable con dos campos: LANGOSTA; CANGREJO. Por defecto debe
estar LANGOSTA.
"""

from core.model.maestro.especie_tipo import EspecieTipo


class Especie(models.Model):



    codigo = models.IntegerField(
                            unique=True,
                            )

    nombre = models.CharField(max_length=255,
                            null=True,
                            blank=True,
                            )

    defecto = models.BooleanField(null=True,
                            blank=True,
                            )




    mt_especie_tipo = models.ForeignKey(
                            EspecieTipo, 
                            on_delete=models.PROTECT,
                            null=True,
                            blank=True,
                         )

    #Es la unidad propuesta, se puede modificar
    mt_unidad = models.ForeignKey(
                            Unidad, 
                            on_delete=models.PROTECT,
                            null=True,
                            blank=True,
                         )





        

    class Meta:
        verbose_name="Especie"
        verbose_name_plural=verbose_name+"s"
        db_table =("mt_"+str(verbose_name).replace(' ','_')).lower()
    
    def __str__(self):
        return str(self.codigo)+'-'+str(self.nombre)



class EspecieSerializer(serializers.ModelSerializer):

    #assert serializers.data == {'especie_tipo': 'def'}
    
    class Meta:
        model = Especie
        fields='__all__'
        #fields = ('username', 'email')
        #extra_kwargs = {'password': {'write_only': True}}


