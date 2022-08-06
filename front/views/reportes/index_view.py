from django.shortcuts import render,redirect
from django.views.generic import View

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from core.model.viaje import Viaje

class IndexView(View):

	def get(self,request,id=None,*args,**kwargs):

		viaje = Viaje.objects.filter(id=id).first()
		registros = Viaje.objects.order_by('-id')

		paginator = Paginator(registros, 20)
		page = request.GET.get('page')


		try:
			items = paginator.page(page)
		except PageNotAnInteger:
			# If page is not an integer, deliver first page.
			items = paginator.page(1)
		except EmptyPage:
			# If page is out of range (e.g. 9999), deliver last page of results.
			items= paginator.page(paginator.num_pages)

	
		return render(request,'reportes/index.html',{'items':items,'page':page,'viaje':viaje})


	
