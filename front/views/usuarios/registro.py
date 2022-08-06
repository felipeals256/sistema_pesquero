from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,UpdateView
from django.urls import reverse_lazy
from django.contrib import messages

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from core.model.viaje import Viaje

from core.model.user import User
from front.forms.user.user_form import UserForm

class CrearView(CreateView):

	model = User
	form_class = UserForm
	template_name="usuarios/create.html"
	success_message = "registro creado"



	def post(self,request,*args,**kwargs):

		form = self.form_class(request.POST)
		if form.is_valid():
			user = User()
			user.email = form.cleaned_data.get('email')
			user.username = form.cleaned_data.get('username')
			user.first_name = form.cleaned_data.get('first_name')
			user.last_name = form.cleaned_data.get('last_name')
			user.pass_local = form.cleaned_data.get('pass_local')
			if form.cleaned_data.get('password1'):
				user.set_password(form.cleaned_data.get('password1'))

			user.is_superuser=False
			if form.cleaned_data.get('user_type'):
				user.user_type = form.cleaned_data.get('user_type')
				if user.user_type.codigo == 1:
					user.is_superuser=True
					
			user.save()
			messages.success(self.request, self.success_message.upper())
			return redirect("usuarios")
		else:
			return render(request,self.template_name,{'form':form})

class ActualizarView(UpdateView):

	model = User
	form_class = UserForm
	template_name="usuarios/create.html"
	success_message = "Cambios realizados"
	#success_url = reverse_lazy("usuarios")




	def post(self,request,pk,*args,**kwargs):
		
		form = self.form_class(request.POST, instance=User.objects.filter(id=pk).first())

		if form.is_valid():

			user = User.objects.filter(id=pk).first()
			user.email = form.cleaned_data.get('email')
			user.username = form.cleaned_data.get('username')
			user.first_name = form.cleaned_data.get('first_name')
			user.last_name = form.cleaned_data.get('last_name')
			user.pass_local = form.cleaned_data.get('pass_local')
			if form.cleaned_data.get('password1'):
				user.set_password(form.cleaned_data.get('password1'))

			user.is_superuser=False
			if form.cleaned_data.get('user_type'):
				user.user_type = form.cleaned_data.get('user_type')
				if user.user_type.codigo == 1:
					user.is_superuser=True

			user.save()
			messages.success(self.request, self.success_message.upper())
			return redirect("usuarios")
		else:
			return render(request,self.template_name,{'form':form})
