from django.http import HttpResponse


def index1(request):
    return HttpResponse("Front page")
