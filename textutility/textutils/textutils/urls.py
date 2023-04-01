"""textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import view
from . import view2
from . import view3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.index, name='index'),
    path('about', view.about, name='about'),
    path('facebook', view2.facebook, name='facebook'),
    path('chatgpt', view3.chatgpt, name='chatgpt'),
    path('w3school', view3.w3school, name='w3school'),
    path('instagram', view3.instagram, name='instagram'),
    path('cricbuzz', view3.cricbuzz, name='cricbuzz'),
    path('flipcart', view3.flipcart, name='flipcart'),
    path('mysite', view2.mysite, name='mysite'),

]
