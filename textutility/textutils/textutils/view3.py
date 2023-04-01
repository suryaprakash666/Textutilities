from django.http import HttpResponse


def chatgpt(request):
    return HttpResponse('''<h2>Visit Chatgpt</h2> <a href="https://chat.openai.com"> Chatgpt</a>''')


def cricbuzz(request):
    return HttpResponse('''<h2>Visit Chatgpt</h2> <a href="https://chat.openai.com"> Chatgpt</a>''')


def instagram(request):
    return HttpResponse('''<h2>Visit Chatgpt</h2> <a href="https://chat.openai.com"> Chatgpt</a>''')


def flipcart(request):
    return HttpResponse("flipcart <a href='/'>back</a>")


def w3school(request):
    return HttpResponse('''<h2>Visit Chatgpt</h2> <a href="https://chat.openai.com"> Chatgpt</a>''')
