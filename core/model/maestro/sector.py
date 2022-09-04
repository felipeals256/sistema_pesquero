from django.db import models


from rest_framework import serializers


class Sector(models.Model):



    nombre = models.CharField(max_length=100,
                            unique=True,
                            verbose_name="nombre",
                            )
    

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    user_modificador=models.ForeignKey(to="core.User",
                                on_delete=models.PROTECT,
                                null=True,
                                blank=True,
                                related_name='+',
                                verbose_name="modificado por",
                            )

    user_creador=models.ForeignKey(to="core.User",
                                related_name='+',
                                on_delete=models.PROTECT,
                                null=True,
                                verbose_name="creado por",
                                blank=True
                            )


 
    class Meta:
        verbose_name="Sector"
        verbose_name_plural=verbose_name+"es"
        db_table =("mt_"+str(verbose_name).replace(' ','_')).lower()
    
    def __str__(self):
        return str(self.nombre)



class SectorSerializer(serializers.ModelSerializer):

    #rut = serializers.SerializerMethodField('getRut')

    
    class Meta:
        model = Sector
        fields='__all__'
        #fields = ('username', 'email')
        #extra_kwargs = {'password': {'write_only': True}}


