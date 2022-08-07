


from django.db import models
from django.core.exceptions import ValidationError

from rest_framework import serializers
from core.model.user import User

from core.model.maestro.bote import Bote
from core.model.maestro.isla import Isla
from core.model.bote_vigencia import BoteVigencia


"""
un bote puede es en más de una isla, pero tienen vijencia, se debe listar un bote en una isla cuando tenga vigencia
"""
class BoteVigenciaHistorico(models.Model):

    bote_vigencia =models.ForeignKey(
                     BoteVigencia, 
                     on_delete=models.PROTECT,
                 )
    mt_bote=models.ForeignKey(
                     Bote, 
                     on_delete=models.PROTECT,
                 )

    #solo una relación entre bote e isla
    mt_isla = models.ForeignKey(
             Isla, 
             on_delete=models.PROTECT,
         )

    #registra la información del id usuario que realiza acciones sobre esta tabla.
    user_modificador=models.ForeignKey(User, 
                                on_delete=models.PROTECT,
                                null=True,
                                blank=True
                            )

    """
    BOTE que no tengan fecha término registro estarán vigentes. Sólo puede existir un registro
    vigente por matrícula. Para dar de baja un BOTE se ingresa la Fecha término registro. Se
    registra la información del id usuario que realiza acciones sobre esta tabla.
    """
    fecha_termino =  models.DateField(
                            null=True,
                            blank=True,
                            )

        

    class Meta:
        verbose_name="Bote Vigencia Historico"
        verbose_name_plural=verbose_name+"s"
        db_table =str(verbose_name).replace(' ','_').lower()
    
    def __str__(self):
        return "Código #"+str(self.id)







