from django.shortcuts import render
from django.http import HttpResponse




def analyzer(request):
    jangotext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'default')
    fullcaps = request.POST.get('fullcaps', 'default')
    if removepunc == 'on':

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in jangotext:
            if char not in punctuations:
                analyzed += char

        params = {'purpose': 'removepuntuation', 'analyzed_text': analyzed}

        return render(request, 'Analyzer.html', params)

    elif (fullcaps == 'on'):
        analyzed = ""
        for char in jangotext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'change to uppercase', 'analyzed_text': analyzed}

        return render(request, 'Analyzer.html', params)
    else:
        return HttpResponse('error')
