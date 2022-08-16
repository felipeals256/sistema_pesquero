from django.contrib import admin

from core.model.maestro.arte import Arte
from core.model.maestro.bote import Bote
from core.model.maestro.especie import Especie
from core.model.maestro.especie_tipo import EspecieTipo
from core.model.maestro.subsistema import Subsistema
from core.model.maestro.sector import Sector
from core.model.maestro.zona import Zona
from core.model.maestro.unidad import Unidad
from core.model.carnada import Carnada
from core.model.bote_vigencia import BoteVigencia

class ArteAdmin(admin.ModelAdmin):
	# con esto muestras los campos que deses al mostrar la lista en admin
    list_display=['codigo', 'descripcion']
    # con esto añades un campo de texto que te permite realizar la busqueda, puedes añadir mas de un atributo por el cual se filtrar
    search_fields = ['codigo', 'descripcion']
    # con esto añadiras una lista desplegable con la que podras filtrar (activo es un atributo booleano)
    #list_filter = ['codigo', 'descripcion']

    readonly_fields = ('user_modificador','user_creador',)
    #metodo que se utiliza al momento de llamar el save()
    def save_model(self, request, obj, form, change):
        obj.user_modificador = request.user
        if not obj.id:
            obj.user_creador = request.user
        super().save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        return False
    


    def get_actions(self, request):
        actions = super(ArteAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

admin.site.register(Arte,ArteAdmin)
	
class BoteAdmin(admin.ModelAdmin):
	# con esto muestras los campos que deses al mostrar la lista en admin
    list_display=['matricula','nombre']
    # con esto añades un campo de texto que te permite realizar la busqueda, puedes añadir mas de un atributo por el cual se filtrar
    search_fields =['matricula','nombre']
    # con esto añadiras una lista desplegable con la que podras filtrar (activo es un atributo booleano)
    #list_filter = [ 'descripcion']
    def has_delete_permission(self, request, obj=None):
        return False

    readonly_fields = ('user_modificador','user_creador',)

    def get_actions(self, request):
        actions = super(BoteAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    #metodo que se utiliza al momento de llamar el save()
    def save_model(self, request, obj, form, change):
        obj.user_modificador = request.user
        if not obj.id:
            obj.user_creador = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Bote,BoteAdmin)


class EspecieAdmin(admin.ModelAdmin):
	# con esto muestras los campos que deses al mostrar la lista en admin
    list_display=['codigo', 'nombre','mt_unidad']
    # con esto añades un campo de texto que te permite realizar la busqueda, puedes añadir mas de un atributo por el cual se filtrar
    search_fields = ['codigo', 'nombre']

    readonly_fields = ('user_modificador','user_creador',)
    #metodo que se utiliza al momento de llamar el save()
    def save_model(self, request, obj, form, change):
        obj.user_modificador = request.user
        if not obj.id:
            obj.user_creador = request.user
        super().save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super(EspecieAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

admin.site.register(Especie,EspecieAdmin)


class SubsistemaAdmin(admin.ModelAdmin):
	# con esto muestras los campos que deses al mostrar la lista en admin
    list_display=['codigo', 'descripcion']
    # con esto añades un campo de texto que te permite realizar la busqueda, puedes añadir mas de un atributo por el cual se filtrar
    search_fields = ['codigo', 'descripcion']
    # con esto añadiras una lista desplegable con la que podras filtrar (activo es un atributo booleano)
    #list_filter = ['es_bycatch']

    readonly_fields = ('user_modificador','user_creador',)
    #metodo que se utiliza al momento de llamar el save()
    def save_model(self, request, obj, form, change):
        obj.user_modificador = request.user
        if not obj.id:
            obj.user_creador = request.user
        super().save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super(SubsistemaAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

admin.site.register(Subsistema,SubsistemaAdmin)


class SectorAdmin(admin.ModelAdmin):
    # con esto muestras los campos que deses al mostrar la lista en admin
    list_display=['nombre']
    # con esto añades un campo de texto que te permite realizar la busqueda, puedes añadir mas de un atributo por el cual se filtrar
    search_fields = ['nombre']
    # con esto añadiras una lista desplegable con la que podras filtrar (activo es un atributo booleano)
    #list_filter = ['es_bycatch']

    readonly_fields = ('user_modificador','user_creador',)
    #metodo que se utiliza al momento de llamar el save()
    def save_model(self, request, obj, form, change):
        obj.user_modificador = request.user
        if not obj.id:
            obj.user_creador = request.user
        super().save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super(SectorAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

admin.site.register(Sector,SectorAdmin)

class ZonaAdmin(admin.ModelAdmin):
    # con esto muestras los campos que deses al mostrar la lista en admin
    list_display=['codigo', 'descripcion']
    # con esto añades un campo de texto que te permite realizar la busqueda, puedes añadir mas de un atributo por el cual se filtrar
    search_fields = ['codigo', 'descripcion']
    # con esto añadiras una lista desplegable con la que podras filtrar (activo es un atributo booleano)
    #list_filter = ['es_bycatch']

    readonly_fields = ('user_modificador','user_creador',)
    #metodo que se utiliza al momento de llamar el save()
    def save_model(self, request, obj, form, change):
        obj.user_modificador = request.user
        if not obj.id:
            obj.user_creador = request.user
        super().save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super(ZonaAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

admin.site.register(Zona,ZonaAdmin)

class UnidadAdmin(admin.ModelAdmin):
    # con esto muestras los campos que deses al mostrar la lista en admin
    list_display=['codigo','unidad', 'descripcion']
    # con esto añades un campo de texto que te permite realizar la busqueda, puedes añadir mas de un atributo por el cual se filtrar
    search_fields = ['codigo','unidad', 'descripcion']
    # con esto añadiras una lista desplegable con la que podras filtrar (activo es un atributo booleano)
    #list_filter = ['es_bycatch']

    readonly_fields = ('user_modificador','user_creador',)
    #metodo que se utiliza al momento de llamar el save()
    def save_model(self, request, obj, form, change):
        obj.user_modificador = request.user
        if not obj.id:
            obj.user_creador = request.user
        super().save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super(UnidadAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
admin.site.register(Unidad,UnidadAdmin)




class EspecieTipoAdmin(admin.ModelAdmin):
    # con esto muestras los campos que deses al mostrar la lista en admin
    list_display=['codigo', 'descripcion']
    # con esto añades un campo de texto que te permite realizar la busqueda, puedes añadir mas de un atributo por el cual se filtrar
    search_fields = ['codigo', 'descripcion']
    # con esto añadiras una lista desplegable con la que podras filtrar (activo es un atributo booleano)
    #list_filter = ['es_bycatch']
    
    readonly_fields = ('user_modificador','user_creador',)
    #metodo que se utiliza al momento de llamar el save()
    def save_model(self, request, obj, form, change):
        obj.user_modificador = request.user
        if not obj.id:
            obj.user_creador = request.user
        super().save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super(EspecieTipoAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

admin.site.register(EspecieTipo,EspecieTipoAdmin)


class BoteVigenciaAdmin(admin.ModelAdmin):
    # con esto muestras los campos que deses al mostrar la lista en admin
    list_display=['mt_bote', 'mt_subsistema','fecha_termino']
    # con esto añades un campo de texto que te permite realizar la busqueda, puedes añadir mas de un atributo por el cual se filtrar
    search_fields = ['mt_bote', 'mt_subsistema','fecha_termino']
    # con esto añadiras una lista desplegable con la que podras filtrar (activo es un atributo booleano)
    #list_filter = ['es_bycatch']
    ordering = ['-fecha_termino']

    list_filter = ['mt_bote', 'mt_subsistema','fecha_termino']

    readonly_fields = ('user_modificador','user_creador',)
    #metodo que se utiliza al momento de llamar el save()
    def save_model(self, request, obj, form, change):
        obj.user_modificador = request.user
        if not obj.id:
            obj.user_creador = request.user
        super().save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super(BoteVigenciaAdmin, self).get_actions(request)

        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions



    def get_readonly_fields(self, request, obj=None): 
   
        #if obj: # editing an existing object 
        #    return self.readonly_fields + ('user_modificador',) 

        return self.readonly_fields

admin.site.register(BoteVigencia,BoteVigenciaAdmin)


