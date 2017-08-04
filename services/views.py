from django.shortcuts import render
from django.views import View


class LandSurveyingView(View):

    def get(self, request):
        context = {}
        return render(request, 'services/landSurveying.html', context)


class CadastralSurveyingView(View):

    def get(self, request):
        context = {}
        return render(request, 'services/cadastral.html', context)


class TopographicalSurveyingView(View):

    def get(self, request):
        context = {}
        return render(request, 'services/topographical.html', context)


class SettingOutView(View):

    def get(self, request):
        context = {}
        return render(request, 'services/settingOut.html', context)


class LevelingView(View):

    def get(self, request):
        context = {}
        return render(request, 'services/leveling.html', context)


class BaseMapView(View):

    def get(self, request):
        context = {}
        return render(request, 'services/baseMap.html', context)


class MapMakingView(View):

    def get(self, request):
        context = {}
        return render(request, 'services/mapMaking.html', context)


class FarmSurveyView(View):

    def get(self, request):
        context = {}
        return render(request, 'services/farmSurvey.html', context)


class FarmLandDivisionView(View):

    def get(self, request):
        context = {}
        return render(request, 'services/farmLandDivision.html', context)


class GeographicalView(View):

    def get(self, request):
        context = {}
        return render(request, 'services/geographical.html', context)


class DatabaseCreationView(View):

    def get(self, request):
        context = {}
        return render(request, 'services/databaseCreation.html', context)


class LandMarketingView(View):

    def get(self, request):
        context = {}
        return render(request, 'services/landMarketing.html', context)


class GeneralConsultancyView(View):

    def get(self, request):
        context = {}
        return render(request, 'services/generalConsultancy.html', context)


class ManufacturingView(View):

    def get(self, request):
        context = {}
        return render(request, 'services/manufacturing.html', context)


class BuildingConstructionView(View):

    def get(self, request):
        context = {}
        return render(request, 'services/buildingConstruction.html', context)


class StructuralWorksView(View):

    def get(self, request):
        context = {}
        return render(request, 'services/structuralWorks.html', context)


class QuantitySurveyingView(View):

    def get(self, request):
        context = {}
        return render(request, 'services/quantitySurveying.html', context)


class RoadConstructionView(View):

    def get(self, request):
        context = {}
        return render(request, 'services/roadConstruction.html', context)


class InfoTechView(View):

    def get(self, request):
        context = {}
        return render(request, 'services/infoTech.html', context)


class ProgrammingView(View):

    def get(self, request):
        context = {}
        return render(request, 'services/programming.html', context)


class NetworkingView(View):

    def get(self, request):
        context = {}
        return render(request, 'services/networking.html', context)


class GraphicsDesignView(View):

    def get(self, request):
        context = {}
        return render(request, 'services/graphics.html', context)


class ServicingView(View):

    def get(self, request):
        context = {}
        return render(request, 'services/servicing.html', context)


class PrintingView(View):

    def get(self, request):
        context = {}
        return render(request, 'services/printing.html', context)
