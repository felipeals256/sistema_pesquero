from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework import serializers
from core.model.user_type import UserType

class User(AbstractUser):


    user_type = models.ForeignKey(
                            UserType, 
                            on_delete=models.PROTECT,
                            null=True,
                            blank=True,
                         )

    pass_local = models.CharField(
                                verbose_name="Contraseña Local",
                                null=True,
                                blank=True,
                                max_length=100,
                            )

    def say_hello(self):
        return "Hello, my name is {}".format(self.first_name)


    def getFullName(self):
        if not self.first_name and not self.last_name:
            return self.username

        return self.first_name+" "+self.last_name

    def __str__(self):
        return str(self.username)


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields='__all__'