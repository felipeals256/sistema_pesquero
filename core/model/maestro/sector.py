from django.db import models


from rest_framework import serializers


class Sector(models.Model):



    codigo = models.IntegerField(
                            unique=True,
                            )

    descripcion = models.CharField(max_length=255,
                            null=True,
                            blank=True,
                            )




 
    class Meta:
        verbose_name="Sector"
        verbose_name_plural=verbose_name+"s"
        db_table =("mt_"+str(verbose_name).replace(' ','_')).lower()
    
    def __str__(self):
        return str(self.codigo)+'-'+str(self.descripcion)



class SectorSerializer(serializers.ModelSerializer):

    #rut = serializers.SerializerMethodField('getRut')

    
    class Meta:
        model = Sector
        fields='__all__'
        #fields = ('username', 'email')
        #extra_kwargs = {'password': {'write_only': True}}


