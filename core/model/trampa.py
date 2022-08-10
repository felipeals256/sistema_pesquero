from django.db import models


from rest_framework import serializers



"""
Trampa: No existe un identificador único de la trampa en el sistema. El que se utiliza es un
correlativo en la bitácora de viaje. Sólo se completa información de la trampa si ésta se ha visitado.
Si no hubo captura, se indica 0. La trampa pertenece a un Sector y a una zona.
"""

from core.model.maestro.sector import Sector
from core.model.maestro.zona import Zona



class Trampa(models.Model):

    codigo = models.IntegerField(
                            unique=True,
                            )
    

    """
    Sector(*): Formato lista desplegable con los sectores de la tabla maestra. Si no lo encuentra,
    debe registrarlo en Observaciones. El sistema le va a proponer los sectores del histórico, pero
    podrá ingresar uno distinto. La aplicación deberá generar un reporte para los investigadores en
    el que señala que el sector cambió.
    """
    mt_sector = models.ForeignKey(
                            Sector, 
                            on_delete=models.PROTECT,
                         )

    mt_zona = models.ForeignKey(
                        Zona, 
                        on_delete=models.PROTECT,
                        )








    def formatearCampos(self):

        return None


        

    class Meta:
        verbose_name="Trampa"
        verbose_name_plural=verbose_name+"s"
        db_table =str(verbose_name).replace(' ','_').lower()
    
    def __str__(self):
        re = str(self.token)
        return re



class TrampaSerializer(serializers.ModelSerializer):

    #rut = serializers.SerializerMethodField('getRut')

    
    class Meta:
        model = Trampa
        fields='__all__'
        #fields = ('username', 'email')
        #extra_kwargs = {'password': {'write_only': True}}


