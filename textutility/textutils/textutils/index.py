from django.http import HttpResponse
from django.shortcuts import render


def index1(request):
    return render(request, 'template.html')
