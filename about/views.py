from django.shortcuts import render


def about(request):
    context = {
        'title': 'ABOUT US'
    }
    return render(request, 'about/index.html', context)
