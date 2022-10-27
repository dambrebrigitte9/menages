from django.urls import path #path function
from . import views # . is shorthand for the current directory
from django.urls import  include ,path


# one urlpattern per line
urlpatterns = [
    path('', views.index, name='index'),
    path('suite', views.brigitte, name='suite'),
    path('fin', views.bibi, name='suite'),
    # path('formulaire_recrute', views.pere, name='formulaire_recrute'),
    path('formulaire_employee', views.form, name='formulaire_employee'),
    path('Nos_services', views.nos_services, name='Nos_services'),
    path('service_netoyage', views.netoie, name='service_netoyage'),
    path('lavage_habit', views.habit, name='lavage_habit'),
    path('form_adheration', views.adheration, name='form_adheration'),
    path('nous_contacter', views.contacter, name='nous_contacter'),
    path('apropos', views.apropo, name='apropos'),
    path('fille_de_menage', views.fille, name='fille_de_menage'),
    path('formulaire_recrute', views.employee, name='formulaire_recrute'),


  
]
