from django.shortcuts import render


def index_page(request):
    context = {
        "title": "welcome to the home page"
    }
    return render(request, 'index/index.html', context)
