from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^manufacturing-and-selling/$', views.ManufacturingView.as_view(), name='manufacturing'),
    url(r'^building-construction/$', views.BuildingConstructionView.as_view(), name='building'),
    url(r'^structural-and-architectural-works/$', views.StructuralWorksView.as_view(), name='structural'),
    url(r'^quantity-surveying/$', views.QuantitySurveyingView.as_view(), name='quantity'),
    url(r'^road-construction/$', views.RoadConstructionView.as_view(), name='road'),

    url(r'^information-technology/$', views.InfoTechView.as_view(), name='information'),

    url(r'^information-technology/software/$', views.StructuralWorksView.as_view(), name='software'),
    url(r'^information-technology/servicing/$', views.QuantitySurveyingView.as_view(), name='servicing'),
    url(r'^information-technology/networking/$', views.RoadConstructionView.as_view(), name='networking'),
    url(r'^information-technology/graphics/$', views.InfoTechView.as_view(), name='graphics'),

    url(r'^land-surveying/$', views.LandSurveyingView.as_view(), name='land'),

    url(r'^land-surveying/cadastral-survey/$', views.CadastralSurveyingView.as_view(), name='cadastral'),
    url(r'^land-surveying/topographical-survey/$', views.TopographicalSurveyingView.as_view(), name='topographical'),
    url(r'^land-surveying/setting-out-of-layout/$', views.SettingOutView.as_view(), name='settingOut'),
    url(r'^land-surveying/leveling/$', views.LevelingView.as_view(), name='leveling'),
    url(r'^land-surveying/base-map-preparation/$', views.BaseMapView.as_view(), name='baseMap'),
    url(r'^land-surveying/map-making/$', views.MapMakingView.as_view(), name='mapMaking'),
    url(r'^land-surveying/farm-survey/$', views.FarmSurveyView.as_view(), name='farmSurvey'),
    url(r'^land-surveying/farm-land-division/$', views.FarmLandDivisionView.as_view(), name='farmLand'),
    url(r'^land-surveying/geographical-information-systems/$', views.GeographicalView.as_view(), name='geographical'),
    url(r'^land-surveying/database-creation/$', views.DatabaseCreationView.as_view(), name='database'),
    url(r'^land-surveying/land-marketing/$', views.LandMarketingView.as_view(), name='landMarketing'),
    url(r'^land-surveying/general-consultancy/$', views.GeneralConsultancyView.as_view(), name='generalConsultancy'),

    url(r'^printing-press/$', views.PrintingView.as_view(), name='printing'),
]
