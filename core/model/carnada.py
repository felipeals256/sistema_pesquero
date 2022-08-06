from django.db import models


from rest_framework import serializers

from core.model.maestro.unidad import Unidad



class Carnada(models.Model):


    codigo = models.IntegerField(
                            unique=True,
                            )
    """
    Especie_CarnadaEspecie: Formato lista desplegable que depende de la especie de captura seleccionada.
    """
    nombre = models.CharField(max_length=100,
                            unique=True,
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
        verbose_name="Carnada"
        verbose_name_plural=verbose_name+"s"
        db_table =(str(verbose_name).replace(' ','_')).lower()
    
    def __str__(self):
        re = str(self.codigo)
        return re



class CarnadaSerializer(serializers.ModelSerializer):

    #rut = serializers.SerializerMethodField('getRut')

    
    class Meta:
        model = Carnada
        fields='__all__'
        #fields = ('username', 'email')
        #extra_kwargs = {'password': {'write_only': True}}


