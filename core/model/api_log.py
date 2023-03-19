from django.db import models


from rest_framework import serializers
from core.model.user import User

class ApiLog(models.Model):

  

    request_data = models.TextField(
                            null=True,
                            blank=True,
                            )

    response_data = models.TextField(
                            null=True,
                            blank=True,
                            )

    fecha_creacion = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name="API Log"
        verbose_name_plural=verbose_name+"s"
        db_table =(""+str(verbose_name).replace(' ','_')).lower()
    
    def __str__(self):
        return str(self.id)






