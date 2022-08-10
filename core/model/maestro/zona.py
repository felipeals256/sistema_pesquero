from django.db import models


from rest_framework import serializers

from core.model.maestro.sector import Sector

class Zona(models.Model):


    codigo = models.IntegerField(
                            unique=True,
                            )

    descripcion = models.CharField(max_length=255,
                            null=True,
                            blank=True,
                            )

    mt_sector = models.ManyToManyField(Sector,)




    def formatearCampos(self):

        return None


        

    class Meta:
        verbose_name="Zona"
        verbose_name_plural=verbose_name+"s"
        db_table =("mt_"+str(verbose_name).replace(' ','_')).lower()
    
    def __str__(self):
        return str(self.codigo)+'-'+str(self.descripcion)



class ZonaSerializer(serializers.ModelSerializer):

    #rut = serializers.SerializerMethodField('getRut')

    
    class Meta:
        model = Zona
        fields='__all__'
        #fields = ('username', 'email')
        #extra_kwargs = {'password': {'write_only': True}}


