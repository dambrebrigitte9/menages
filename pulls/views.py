from email import message
from multiprocessing.spawn import is_forking
from django.shortcuts import render
from django.http import  HttpResponseRedirect,  HttpResponse
from pulls.models import Employee,Service,nous_contacter
from pulls.forms import EmployeeForm,ServiceForm

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
# from EmployeeForm import EmployeeForm





# Create your views here.

from django.shortcuts import render # this line is added automatically
from django.http import HttpResponse # pass view information into the browser

# takes a request, returns a response


from django.shortcuts import render # this line is added automatically
from django.http import HttpResponse # pass view information into the browser

# takes a request, returns a response
from .forms import EmployeeForm



def index(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        titre = request.POST.get('titre')
        laisser_un_message=request.POST.get('laisser_un_message')
        


        donnees = nous_contacter.objects.create(email=email,  
        first_name=first_name, titre=titre,
        laisser_un_message=laisser_un_message)
                        
        donnees.save()
       
    return render(request, 'posts/index.html',{'form':form})

    

    # return render(request, 'posts/index.html')



def brigitte(request):
    

   
    return render(request, 'posts/portfolio-details.html')



def bibi(request):
    

   
    return render(request, 'posts/posts.html')




# def pere(request):
#     user = {
#         'first_name' : "John",
#         'last_name' : "Doe"
#     } 

#     subjects = [
#         {
#             'title' : "projet",
#             'author': "Brigitte"
#         },
#         {
#             'title' : "ma page d'accueil",
#             'author' : "Brigitte"
#         }
#     ]

#     context = {
#         'user' : user,
#         'subjects': subjects
#     }
#     return render(request, 'posts/formulaire_recrute.html')


def form(request):
    

   
    return render(request, 'posts/formulaire_employee.html')



    # def Nos_services(request):
    #     template = loader.get_template('Nos_services.html')
    # return HttpResponse(template.render())



def nos_services(request):
    

   
    return render(request, 'posts/Nos_services.html')





def netoie(request):
    

   
    return render(request, 'posts/service_netoyage.html')





def habit(request):
    

   
    return render(request, 'posts/lavage_habit.html')





# def form_adheration(request):
#     user = {
#         'first_name' : "John",
#         'last_name' : "Doe"
#     } 

#     subjects = [
#         {
#             'title' : "projet",
#             'author': "Brigitte"
#         },
#         {
#             'title' : "ma page d'accueil",
#             'author' : "Brigitte"
#         }
#     ]

#     context = {
#         'user' : user,
#         'subjects': subjects
#     }
#     return render(request, 'posts/form_adheration.html')



def contacter(request):
    

   
    return render(request, 'posts/nous_contacter.html')



def apropo(request):
    

   
    return render(request, 'posts/apropos.html')



def form(request):
    

   
    return render(request, 'posts/formulaire_employee.html')


def fille(request):
    

   
    return render(request, 'posts/fille_de_menage.html')



# def employee(request):
#     form=EmployeeForm()
#     if request.method=='POST':
#         form=EmployeeForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             new=Employee.object.create(**form.cleaned_data)
#             new.save()
#             return HttpResponseRedirect("formulaire_recrute")
#     else:
#         form=EmployeeForm()
#         # return render(request,formulaire_recrute.html )

#     return render(request, 'posts/formulaire_recrute.html',{'form':form})


def redirection(request):
    

   
    return render(request, 'posts/redirection.html')



def employee(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        langage_habituel = request.POST.get('langage_habituel')
        annee_de_naissance = request.POST.get('annee_de_naissance')
        numero_employee= request.POST.get('numero_employee')
        emplacement=request.POST.get('emplacement')
        genre = request.POST.get('genre')
        statut=request.POST.get('statut')
        commentaire_sur_savoir_faire=request.POST.get('commentaire_sur_savoir_faire')
        votre_cv=request.POST.get('votre_cv')
       


        donnees = Employee.objects.create(email=email, last_name=last_name, 
        first_name=first_name, langage_habituel=langage_habituel, annee_de_naissance=annee_de_naissance,
        numero_employee=numero_employee, emplacement=emplacement ,genre=genre,
        statut=statut, commentaire_sur_savoir_faire=commentaire_sur_savoir_faire, votre_cv=votre_cv)
                        
        donnees.save()
       
    return render(request, 'posts/formulaire_recrute.html',{'form':form})




def adheration(request):
    if request.method == "POST":
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        email = request.POST.get('email')
        telephone_principale=request.POST.get('telephone_principale')
        telephone_secondaire=request.POST.get('telephone_secondaire')
        emplacement=request.POST.get('emplacement')
        ville=request.POST.get('ville')
        langage_habituel = request.POST.get('langage_habituel')
        service_choisis = request.POST.get('service_choisis')
        option= request.POST.get('moment_pour_vous_contacter')



        donnees = Service.objects.create(email=email, last_name=last_name, 
        first_name=first_name, langage_habituel=langage_habituel, ville=ville,
        telephone_principale=telephone_principale,telephone_secondaire=telephone_secondaire,  emplacement=emplacement ,
        service_choisis=service_choisis, option=option)
                        
        
        donnees.save()

    return render(request, 'posts/form_adheration.html',{'form':form})







# class EmployeeImage(TemplateView):
#     form = EmployeeForm
#     template_name = 'votre_cv.html'

#     def post(self, request, *args, **kwargs):
#         form = EmployeeForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse_lazy('home', kwargs={'pk': pk}))
#         context = self.get_context_data(form=form)
#         return self.render_to_response(context)   
          

#     def get(self, request, *args, **kwargs):
#         return self.post(request, *args, **kwargs)

def votre_cv(request):
    

   
    return render(request, 'posts/votre_cv.html')

def fauteuille(request):
    

   
    return render(request, 'posts/fauteuille_en_cuir.html')













