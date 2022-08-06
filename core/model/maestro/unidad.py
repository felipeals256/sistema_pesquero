from django.db import models


from rest_framework import serializers


class Unidad(models.Model):



    codigo = models.IntegerField(
                            unique=True,
                            )

    unidad = models.CharField(max_length=5,
                            unique=True,
                            null=True,
                            blank=True,
                            )

    descripcion = models.CharField(max_length=255,
                            null=True,
                            blank=True,
                            )




    def formatearCampos(self):

        return None


        

    class Meta:
        verbose_name="Unidad"
        verbose_name_plural=verbose_name+"es"
        db_table =("mt_"+str(verbose_name).replace(' ','_')).lower()
    
    def __str__(self):
        return str(self.codigo)+'-'+str(self.descripcion)



class UnidadSerializer(serializers.ModelSerializer):

    #rut = serializers.SerializerMethodField('getRut')

    
    class Meta:
        model = Unidad
        fields='__all__'
        #fields = ('username', 'email')
        #extra_kwargs = {'password': {'write_only': True}}


