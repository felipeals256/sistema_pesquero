from django.db import models
#from nucleo.models import User
from django.db.models.query import QuerySet
from django.forms import ModelForm as _ModelFrom
from django.conf import settings

from django.utils import timezone

from django.db import connection

#from nucleo.submodels.utilidades.funcion import Funcion
# Create your models here.

class SoftDeletionQuerySet(QuerySet):
	def delete(self):
		return super(SoftDeletionQuerySet, self).update(deleted_at=timezone.now())

	def hard_delete(self):
		return super(SoftDeletionQuerySet, self).delete()

	def alive(self):
		return self.filter(deleted_at=None)

	def dead(self):
		return self.exclude(deleted_at=None)

class SoftDeletionManager(models.Manager):

	def __init__(self, *args, **kwargs):
		self.alive_only = kwargs.pop('alive_only', True)
		super(SoftDeletionManager, self).__init__(*args, **kwargs)

	def get_queryset(self):
		if self.alive_only:
			return SoftDeletionQuerySet(self.model).filter(deleted_at=None)
		return SoftDeletionQuerySet(self.model)

	def hard_delete(self):
		return self.get_queryset().hard_delete()


class Base(models.Model):

    
	objects = SoftDeletionManager()#ejecuta las query obteniendo solo los objetos que no tienen el campo deleted_at
	all_objects = SoftDeletionManager(alive_only=False)#ejecuta las query obteniendo todos los objetos
	#funcion = Funcion()#obtiene diferentes funciones que peden ser útiles

	created_at = models.DateTimeField(auto_now_add=True,
									verbose_name="Fecha creación")
	
	updated_at = models.DateTimeField(auto_now=True,
										blank=True,
										null=True,
										verbose_name="Fecha modificado")
	deleted_at = models.DateTimeField(blank=True,
										null=True,
										verbose_name="Fecha eliminación")



	user_created = models.ForeignKey(settings.AUTH_USER_MODEL,
										blank=True,
										null=True,
										verbose_name="Usuario creador",
										related_name='+',
										on_delete=models.PROTECT)

	user_updated = models.ForeignKey(settings.AUTH_USER_MODEL,
											blank=True,
											null=True,
											verbose_name="Usuario modificador",
											related_name='+',
											on_delete=models.PROTECT)
	user_deleted = models.ForeignKey(settings.AUTH_USER_MODEL,
											blank=True,
											null=True,
											verbose_name="Usuario eliminación",
											related_name='+',
											on_delete=models.PROTECT)

	



	class Meta:

		abstract = True


	#eliminación lógica
	#ej: Pais.objects.get(pk=48).delete(request)
	def delete(self,request=None):#sobreescribimos el metodo delete

		
		if request!=None: #si no existe request no se agrega el usuario de la sesión
			if request.user.is_authenticated: #si si el usuario no está logueado no se agrega el usuario de la sesión
				self.user_deleted=request.user
	

		self.deleted_at = timezone.now()
		super().save()

	#eliminación real
	#ejemplo
	#Pais.objects.get(pk=46).hard_delete()
	def hard_delete(self):
		super(Base, self).delete()

	#elimina todos los registros de forma fisica
	#ej: Pais.delete_all(Pais)
	def delete_all(model):
		cursor = connection.cursor()
		table_name = model._meta.db_table
	
		sql = "DELETE FROM %s;" % (table_name, )
		cursor.execute(sql)

		sql ="ALTER SEQUENCE "+table_name+"_id_seq RESTART WITH 1;" 
		cursor.execute(sql)
    	

	
	def save(self,request=None, *args, **kwargs):
	
	 	if request!=None: #si no existe request no se agrega el usuario de la sesión
	 		if request.user.is_authenticated: #si si el usuario no está logueado no se agrega el usuario de la sesión
	 			self.user_updated=request.user
	 			self.updated_at = timezone.now()

	 	if self.id == None and request!=None:#si el objeto no tiene id quiere secir que es un objeto nuevo
	 		if request.user.is_authenticated: #si si el usuario no está logueado no se agrega el usuario de la sesión
	 			self.user_created=request.user

	 	self.deleted_at=None
	 	self.user_deleted=None

	 	super().save(*args, **kwargs)
	


class ModelForm(_ModelFrom):

    def save(self,request=None):

        object = super().save(commit=False)
        object.save(request)

        return super().save()












