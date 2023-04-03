from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'template.html')


def analyzer(request):
    jangotext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'default')
    print(removepunc)
    print(jangotext)
    if removepunc == 'on':

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in jangotext:
            if char not in punctuations:
                analyzed += char

        params = {'purpose': 'removepuntuation', 'analyzed_text': analyzed}

        return render(request, 'Analyzer.html', params)
    else:
        return HttpResponse('error')
