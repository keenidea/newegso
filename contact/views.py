from django.shortcuts import render


def contact(request):
    context = {
        'title': 'CONTACT US'
    }
    return render(request, 'contact/index.html', context)
