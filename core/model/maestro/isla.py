from django.db import models


from rest_framework import serializers


class Isla(models.Model):




    codigo = models.CharField(
                            unique=True,
                            max_length=3,
                            verbose_name="código",
                            )

    descripcion = models.CharField(max_length=255,
                            null=True,
                            blank=True,
                            verbose_name="descripción",
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
        verbose_name="Isla"
        verbose_name_plural=verbose_name+"s"
        db_table =("mt_"+str(verbose_name).replace(' ','_')).lower()
    
    def __str__(self):
        return str(self.codigo)+'-'+str(self.descripcion)



class IslaSerializer(serializers.ModelSerializer):

    #rut = serializers.SerializerMethodField('getRut')

    
    class Meta:
        model = Isla
        fields='__all__'
        #fields = ('username', 'email')
        #extra_kwargs = {'password': {'write_only': True}}


