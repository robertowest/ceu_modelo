from django.urls import path

from . import views

app_name = 'tablon'

urlpatterns = [
    path('', views.index, name='index'),
    
    path('<slug>', views.tablon),
]
