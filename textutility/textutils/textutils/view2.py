from django.http import HttpResponse
from django.shortcuts import render


def facebook(request):
    return HttpResponse('''<h2>Checkout facebook</h2> <a href="https://www.facebook.com">Facebook.com </a>''')


def mysite(request):
    data = {'name': 'surya', 'address': 'pluto'}
    return render(request, 'template.html', data)
