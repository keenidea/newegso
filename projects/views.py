from django.shortcuts import render
from django.views import View


class CompletedView(View):

    def get(self, request,  *args, **kwargs):
        context = {}
        return render(request, 'projects/completed.html', context)


class UnderDevelopmentView(View):

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'projects/development.html', context)
