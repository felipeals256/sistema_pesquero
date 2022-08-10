from django.db import models


from rest_framework import serializers

"""
Tipo Especie: agrupación de las especies, son tres tipos: crustáceos, moluscos, peces.
"""

class EspecieTipo(models.Model):

    codigo = models.IntegerField(
                            unique=True,
                            )

    descripcion = models.CharField(max_length=255,
                            null=True,
                            blank=True,
                            )




        

    class Meta:
        verbose_name="Tipo de Especie"
        verbose_name_plural=verbose_name+"s"
        db_table =("mt_especie_tipo")
    
    def __str__(self):
        return str(self.codigo)+'-'+str(self.descripcion)



class EspecieTipoSerializer(serializers.ModelSerializer):

    #rut = serializers.SerializerMethodField('getRut')

    
    class Meta:
        model = EspecieTipo
        fields='__all__'
        #fields = ('username', 'email')
        #extra_kwargs = {'password': {'write_only': True}}


