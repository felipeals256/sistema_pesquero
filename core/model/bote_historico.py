from django.db import models


from rest_framework import serializers
from core.model.user import User

class BoteHistorico(models.Model):

    mt_bote=models.ForeignKey(
                     to = 'core.bote', 
                     related_name="bote_id",
                     on_delete=models.PROTECT,
                 )


    numero = models.IntegerField()
    matricula = models.IntegerField()

    nombre = models.CharField(max_length=100,
                            null=True,
                            blank=True,
                            )

    propietario = models.CharField(max_length=255,
                            null=True,
                            blank=True,
                            )

    materialidad = models.CharField(max_length=255,
                            null=True,
                            blank=True,
                            )

    manga = models.IntegerField(
                            null=True,
                            blank=True,
                            )
    eslora = models.IntegerField(
                            null=True,
                            blank=True,
                            )
    forma = models.CharField(max_length=255,
                            null=True,
                            blank=True,
                            )
    rpa = models.CharField(max_length=255,
                            null=True,
                            blank=True,
                            )

    observaciones = models.CharField(max_length=255,
                            null=True,
                            blank=True,
                            )

    descripcion = models.CharField(max_length=255,
                            null=True,
                            blank=True,
                            )

    fecha_cambio = models.DateTimeField(auto_now_add=True)

    #es el usuario que hizo la modificacion en este registro
    user_modificador=models.ForeignKey(User, 
                                on_delete=models.PROTECT,
                                null=True,
                                blank=True,
                                verbose_name="modificado por",
                            )


    class Meta:
        verbose_name="Bote Historico"
        verbose_name_plural=verbose_name+"s"
        db_table =("mt_"+str(verbose_name).replace(' ','_')).lower()
    
    def __str__(self):
        return str(self.numero)+'-'+str(self.descripcion)



class BoteSerializer(serializers.ModelSerializer):

    #rut = serializers.SerializerMethodField('getRut')

    
    class Meta:
        model = BoteHistorico
        fields='__all__'
        #fields = ('username', 'email')
        #extra_kwargs = {'password': {'write_only': True}}


