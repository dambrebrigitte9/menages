from dataclasses import field, fields
from pyexpat import model
from pulls.models import Employee
from pulls.models import Service

from django import forms

class EmployeeForm(forms.Form):
    # genre=forms.CharField(
    #     required=False, 
    #     # validators=[validate_prenom], # Call the validate_nom function here
    #     widget = forms.TextInput(
    #         attrs={
    #             'placeholder': 'Entrer votre genre ici'
    #         })
    #     )

    # first_name = forms.CharField(
    #     required=False, 
    #     # validators=[validate_prenom], # Call the validate_nom function here
    #     widget = forms.TextInput(
    #         attrs={
    #             'placeholder': 'Entrer votre prenom ici'
    #         })
    #     )

    # last_name=forms.CharField(
    #     required=False, 
    #     # validators=[validate_prenom], # Call the validate_nom function here
    #     widget = forms.TextInput(
    #         attrs={
    #             'placeholder': 'Entrer votre prenom Nom'
    #         })
    #     )

    # e_mail=forms.CharField(
    #     required=False, 
    #     # validators=[validate_prenom], # Call the validate_nom function here
    #     widget = forms.EmailInput(
    #         attrs={
    #             'placeholder': 'Entrer votre prenom email'
    #         })
    #     )

    # langage_habituel=forms.CharField(
    #     required=False, 
    #     # validators=[validate_prenom], # Call the validate_nom function here
    #     widget = forms.TextInput(
    #         attrs={
    #             'placeholder': 'Entrer votre prenom Nom'
    #         })
    #     )

    # annee_de_naissance=forms.DateField(
    #     required=False, 
    #     # validators=[validate_prenom], # Call the validate_nom function here
    #     widget = forms.TextInput(
    #         attrs={
    #             'placeholder': 'Entrer votre annee de naissance'
    #         })
    #     )

    # numero_employee=forms.DateField(
    #     required=False, 
    #     # validators=[validate_prenom], # Call the validate_nom function here
    #     widget = forms.TextInput(
    #         attrs={
    #             'placeholder': 'Entrer le numero des employee '
    #         })
    #     )

    # emplacement=forms.CharField(
    #     required=False, 
    #     # validators=[validate_prenom], # Call the validate_nom function here
    #     widget = forms.TextInput(
    #         attrs={
    #             'placeholder': 'Entrer votre emplacement'
    #         })
    #     )

    # statut=forms.CharField(
    #     required=False, 
    #     # validators=[validate_prenom], # Call the validate_nom function here
    #     widget = forms.TextInput(
    #         attrs={
    #             'placeholder': 'Entrer votre Statut'
    #         })
    #     )

    # commentaire_sur_savoir_faire=forms.CharField(
    #         widget = forms.Textarea(
    #             attrs={
    #                 'placeholder': 'Write your comment here'
    #             })
    #         )

    class Meta:
        model=Employee
        fields='__all__'




class ServiceForm(forms.Form):


    class Meta:
        model=Service
        fields='__all__'
