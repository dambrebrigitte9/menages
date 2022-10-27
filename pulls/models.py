from email.policy import default
from random import choices
from secrets import choice
from django.db import models

# Create your models here.


from datetime import datetime, date


# Create your models here.
from django.db import models #import the models package. This line is already existing as soon as we use 'startapp'
from django.db.models import IntegerField, Model
from django.core.validators import  MaxValueValidator, MinValueValidator 
#Must inherit from Django Model class
class Employee(models.Model):
    GENRE = (("HOMME",'HOMME'),("FEMME","FEMME"))
    genre=models.CharField(max_length=30,choices=GENRE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email=models.CharField(max_length=40, default="admin@default.com")
    langage_habituel=models.CharField(max_length=30)
    annee_de_naissance=models.DateField()
    numero_employee=models.CharField(max_length=10)
    emplacement=models.CharField(max_length=30)
    statut=models.CharField(max_length=30,default="Etudiante" )
    commentaire_sur_savoir_faire=models.CharField(max_length=200,
    default="je sais cuisiner")
    
    
    def __str__(self):
        return self.last_name


class Service(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email=models.EmailField(max_length=40, default="admin@default.com")
    telephone_principale=models.CharField(max_length=8, default="73693576")
    telephone_secondaire=models.CharField(max_length=8, null=True)
    emplacement=models.CharField(max_length=30)
    ville=models.CharField(max_length=40)
    langage_habituel=models.CharField(max_length=30)
    service_choisis=models.CharField(max_length=50)



    def __str__(self):
        return self.first_name






