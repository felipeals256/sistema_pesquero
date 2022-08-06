from django import forms
from core.model.user import User
import re

class UserForm(forms.ModelForm):

	#def __init__(self, *args, **kwargs):
	#	user = kwargs.pop("user")
	#	super(UserProfileUpdateForm, self).__init__(*args, **kwargs)

	password1 = forms.CharField(label="Contraseña",required=False,widget=forms.PasswordInput(
			attrs={
				'class':'form form-control',
				#'required':'required'
			}
		))

	password2 = forms.CharField(label="Confirmación de Contraseña" ,required=False,widget=forms.PasswordInput(
			attrs={
				'class':'form form-control',
				#'required':'required'
			}
		))

	"""
		Se valida la contraseña de la web
		Agrega una validación
	"""
	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')

		if (password1 or password2) and password1 != password2 :
			raise forms.ValidationError('Las contraseñas de la web no coinciden')

		return password2

	



		


	class Meta:
		model = User
		fields = ['username','first_name','last_name','email','pass_local','user_type']
		widgets = {

			'username':forms.TextInput(
					attrs={
					 'class':'form form-control'
					}
				),
			'email':forms.EmailInput(
					attrs={
					 'class':'form form-control'
					}
				),
			'first_name':forms.TextInput(
					attrs={
					 'class':'form form-control'
					}
				),
			'last_name':forms.TextInput(
					attrs={
					 'class':'form form-control'
					}
				),
			'user_type':forms.Select(

					attrs={
					 'class':'form form-control',
					 'required':'required'
					}
				),
			'pass_local':forms.TextInput(
					attrs={
					 'class':'form form-control'
					}
				),
		}