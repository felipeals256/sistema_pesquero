from django.db import models


from rest_framework import serializers

from core.model.maestro.unidad import Unidad



class UserType(models.Model):


    codigo = models.IntegerField(
                            unique=True,
                            )
    """
    Especie_CarnadaEspecie: Formato lista desplegable que depende de la especie de captura seleccionada.
    """
    nombre = models.CharField(max_length=100,
                            unique=True,
                            null=True,
                            blank=True,
                            )

    
        

    class Meta:
        verbose_name="Tipo de Usuario"
        verbose_name_plural="Tipos de Usuarios"
        db_table ="user_type"
    
    def __str__(self):
        re = str(self.nombre)
        return re



class UserTypeSerializer(serializers.ModelSerializer):

    #rut = serializers.SerializerMethodField('getRut')

    
    class Meta:
        model = UserType
        fields='__all__'
        #fields = ('username', 'email')
        #extra_kwargs = {'password': {'write_only': True}}


