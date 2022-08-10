from django.db import models


from rest_framework import serializers



"""
BOTE: Se administrará un histórico del bote, con sus características actualizadas desde el
archivo CTM al comienzo de la temporada. Si se modifica alguna característica, se crea un
nuevo registro y al anterior se le ingresa Fecha término registro. Todos los registros de la tabla
BOTE que no tengan fecha término registro estarán vigentes. Sólo puede existir un registro
vigente por matrícula. Para dar de baja un BOTE se ingresa la Fecha término registro. Se
registra la información del id usuario que realiza acciones sobre esta tabla.
"""
class Bote(models.Model):


    numero = models.IntegerField(
                            unique=True,
                            )

    descripcion = models.CharField(max_length=255,
                            null=True,
                            blank=True,
                            )

    rpa = models.CharField(max_length=255,
                            null=True,
                            blank=True,
                            )
    

    


        

    class Meta:
        verbose_name="Bote"
        verbose_name_plural=verbose_name+"s"
        db_table =("mt_"+str(verbose_name).replace(' ','_')).lower()
    
    def __str__(self):
        return str(self.numero)+'-'+str(self.descripcion)



class BoteSerializer(serializers.ModelSerializer):

    #rut = serializers.SerializerMethodField('getRut')

    
    class Meta:
        model = Bote
        fields='__all__'
        #fields = ('username', 'email')
        #extra_kwargs = {'password': {'write_only': True}}


