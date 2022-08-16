from django.db import models


from rest_framework import serializers

from core.model.bote_historico import BoteHistorico

"""
BOTE: Se administrará un histórico del bote, con sus características actualizadas desde el
archivo CTM al comienzo de la temporada. Si se modifica alguna característica, se crea un
nuevo registro y al anterior se le ingresa Fecha término registro. Todos los registros de la tabla
BOTE que no tengan fecha término registro estarán vigentes. Sólo puede existir un registro
vigente por matrícula. Para dar de baja un BOTE se ingresa la Fecha término registro. Se
registra la información del id usuario que realiza acciones sobre esta tabla.
"""
class Bote(models.Model):


    matricula = models.IntegerField(
                            unique=True,
                            verbose_name="matrícula",
                            )

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
    
    
    def save(self):

        bote=Bote.objects.filter(id=self.id).first()
        if bote:
            historico = BoteHistorico()
            historico.mt_bote           = bote
            historico.matricula         = bote.matricula
            historico.nombre            = bote.nombre
            historico.propietario       = bote.propietario
            historico.materialidad      = bote.materialidad
            historico.manga             = bote.manga
            historico.eslora            = bote.eslora
            historico.forma             = bote.forma
            historico.rpa               = bote.rpa
            historico.observaciones     = bote.observaciones
            historico.user_modificador  = bote.user_modificador
            historico.save()

        super().save()
        
        #print(self._meta.db_table)
        #print(bote_historico._meta.db_table)
        
    


        

    class Meta:
        verbose_name="Bote"
        verbose_name_plural=verbose_name+"s"
        db_table =("mt_"+str(verbose_name).replace(' ','_')).lower()
    
    def __str__(self):
        return str(self.matricula)+'-'+str(self.nombre)



class BoteSerializer(serializers.ModelSerializer):

    #rut = serializers.SerializerMethodField('getRut')

    
    class Meta:
        model = Bote
        fields='__all__'
        #fields = ('username', 'email')
        #extra_kwargs = {'password': {'write_only': True}}


