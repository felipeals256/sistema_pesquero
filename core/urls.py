
from django.urls import path

from core.apiview.v1.maestro.arte import ArteView
from core.apiview.v1.maestro.bote import BoteView
from core.apiview.v1.maestro.especie import EspecieView
from core.apiview.v1.maestro.especie_tipo import EspecieTipoView
from core.apiview.v1.maestro.subsistema import SubsistemaView
from core.apiview.v1.maestro.sector import SectorView
from core.apiview.v1.sector_by import SectorByView
from core.apiview.v1.maestro.unidad import UnidadView
from core.apiview.v1.maestro.zona import ZonaView
from core.apiview.v1.bote_vigencia import BoteVigenciaView
from core.apiview.v1.carnada import CarnadaView
from core.apiview.v1.trampa import TrampaView
from core.apiview.v1.trampa_historico import TrampaHistoricoView
from core.apiview.v1.viaje import ViajeView
from core.apiview.v1.user import UserView
from core.apiview.v1.user_type import UserTypeView

from core.apiview.v1.front.subsistema_bote import SubsistemaBoteView

urls_core = ([

    path('v1/arte/', ArteView.as_view() ),
    path('v1/arte/<pk>', ArteView.as_view() ),
    path('v1/bote/', BoteView.as_view() ),
    path('v1/bote/<pk>', BoteView.as_view() ),
    path('v1/especie/', EspecieView.as_view() ),
    path('v1/especie/<pk>', EspecieView.as_view() ),
    path('v1/especie_tipo/', EspecieTipoView.as_view() ),
    path('v1/especie_tipo/<pk>', EspecieTipoView.as_view() ),
    path('v1/subsistema/', SubsistemaView.as_view() ),
    path('v1/subsistema/<pk>', SubsistemaView.as_view() ),
    path('v1/sector/', SectorView.as_view() ),
    path('v1/sector/by/<parametro>/<pk>/', SectorByView.as_view() ),
    path('v1/sector/<pk>', SectorView.as_view() ),
    path('v1/unidad/', UnidadView.as_view() ),
    path('v1/unidad/<pk>', UnidadView.as_view() ),
    path('v1/zona/', ZonaView.as_view() ),
    path('v1/zona/<pk>', ZonaView.as_view() ),
    path('v1/bote_vigencia/', BoteVigenciaView.as_view() ),
    path('v1/bote_vigencia/<pk>', BoteVigenciaView.as_view() ),
    path('v1/carnada/', CarnadaView.as_view() ),
    path('v1/carnada/<pk>', CarnadaView.as_view() ),
    path('v1/trampa/', TrampaView.as_view() ),
    path('v1/trampa/<pk>', TrampaView.as_view() ),
    path('v1/trampa_historico/', TrampaHistoricoView.as_view() ),
    path('v1/trampa_historico/<pk>', TrampaHistoricoView.as_view() ),

    path('v1/viaje/', ViajeView.as_view() ),

    path('v1/user/', UserView.as_view() ),
    path('v1/user/<pk>', UserView.as_view() ),
    path('v1/user_type/', UserTypeView.as_view() ),
    path('v1/user_type/<pk>', UserTypeView.as_view() ),


    path('v1/front/subsistema_bote/<pk>',SubsistemaBoteView.as_view())

    
],"core")