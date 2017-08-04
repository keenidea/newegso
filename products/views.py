from django.shortcuts import render
from django.views import View


class ProductView(View):

    def get(self, request,  *args, **kwargs):
        context = {}
        return render(request, 'products/index.html', context)
