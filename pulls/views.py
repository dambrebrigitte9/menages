from multiprocessing.spawn import is_forking
from django.shortcuts import render
from django.http import  HttpResponseRedirect,  HttpResponse
from pulls.models import Employee,Service
from pulls.forms import EmployeeForm,ServiceForm





# Create your views here.

from django.shortcuts import render # this line is added automatically
from django.http import HttpResponse # pass view information into the browser

# takes a request, returns a response


from django.shortcuts import render # this line is added automatically
from django.http import HttpResponse # pass view information into the browser

# takes a request, returns a response
from .forms import EmployeeForm



def index(request):
    user = {
        'first_name' : "John",
        'last_name' : "Doe"
    } 

    subjects = [
        {
            'title' : "projet",
            'author': "Brigitte"
        },
        {
            'title' : "ma page d'accueil",
            'author' : "Brigitte"
        }
    ]

    context = {
        'user' : user,
        'subjects': subjects
    }
    return render(request, 'posts/index.html', context)



def brigitte(request):
    user = {
        'first_name' : "John",
        'last_name' : "Doe"
    } 

    subjects = [
        {
            'title' : "projet",
            'author': "Brigitte"
        },
        {
            'title' : "ma page d'accueil",
            'author' : "Brigitte"
        }
    ]

    context = {
        'user' : user,
        'subjects': subjects
    }
    return render(request, 'posts/portfolio-details.html', context)



def bibi(request):
    user = {
        'first_name' : "John",
        'last_name' : "Doe"
    } 

    subjects = [
        {
            'title' : "projet",
            'author': "Brigitte"
        },
        {
            'title' : "ma page d'accueil",
            'author' : "Brigitte"
        }
    ]

    context = {
        'user' : user,
        'subjects': subjects
    }
    return render(request, 'posts/posts.html', context)




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
#     return render(request, 'posts/formulaire_recrute.html', context)


def form(request):
    user = {
        'first_name' : "John",
        'last_name' : "Doe"
    } 

    subjects = [
        {
            'title' : "projet",
            'author': "Brigitte"
        },
        {
            'title' : "ma page d'accueil",
            'author' : "Brigitte"
        }
    ]

    context = {
        'user' : user,
        'subjects': subjects
    }
    return render(request, 'posts/formulaire_employee.html', context)



    # def Nos_services(request):
    #     template = loader.get_template('Nos_services.html')
    # return HttpResponse(template.render())



def nos_services(request):
    user = {
        'first_name' : "John",
        'last_name' : "Doe"
    } 

    subjects = [
        {
            'title' : "projet",
            'author': "Brigitte"
        },
        {
            'title' : "ma page d'accueil",
            'author' : "Brigitte"
        }
    ]

    context = {
        'user' : user,
        'subjects': subjects
    }
    return render(request, 'posts/Nos_services.html', context)





def netoie(request):
    user = {
        'first_name' : "John",
        'last_name' : "Doe"
    } 

    subjects = [
        {
            'title' : "projet",
            'author': "Brigitte"
        },
        {
            'title' : "ma page d'accueil",
            'author' : "Brigitte"
        }
    ]

    context = {
        'user' : user,
        'subjects': subjects
    }
    return render(request, 'posts/service_netoyage.html', context)





def habit(request):
    user = {
        'first_name' : "John",
        'last_name' : "Doe"
    } 

    subjects = [
        {
            'title' : "projet",
            'author': "Brigitte"
        },
        {
            'title' : "ma page d'accueil",
            'author' : "Brigitte"
        }
    ]

    context = {
        'user' : user,
        'subjects': subjects
    }
    return render(request, 'posts/lavage_habit.html', context)





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
#     return render(request, 'posts/form_adheration.html', context)



def contacter(request):
    user = {
        'first_name' : "John",
        'last_name' : "Doe"
    } 

    subjects = [
        {
            'title' : "projet",
            'author': "Brigitte"
        },
        {
            'title' : "ma page d'accueil",
            'author' : "Brigitte"
        }
    ]

    context = {
        'user' : user,
        'subjects': subjects
    }
    return render(request, 'posts/nous_contacter.html', context)



def apropo(request):
    user = {
        'first_name' : "John",
        'last_name' : "Doe"
    } 

    subjects = [
        {
            'title' : "projet",
            'author': "Brigitte"
        },
        {
            'title' : "ma page d'accueil",
            'author' : "Brigitte"
        }
    ]

    context = {
        'user' : user,
        'subjects': subjects
    }
    return render(request, 'posts/apropos.html', context)



def form(request):
    user = {
        'first_name' : "John",
        'last_name' : "Doe"
    } 

    subjects = [
        {
            'title' : "projet",
            'author': "Brigitte"
        },
        {
            'title' : "ma page d'accueil",
            'author' : "Brigitte"
        }
    ]

    context = {
        'user' : user,
        'subjects': subjects
    }
    return render(request, 'posts/formulaire_employee.html', context)


def fille(request):
    user = {
        'first_name' : "John",
        'last_name' : "Doe"
    } 

    subjects = [
        {
            'title' : "projet",
            'author': "Brigitte"
        },
        {
            'title' : "ma page d'accueil",
            'author' : "Brigitte"
        }
    ]

    context = {
        'user' : user,
        'subjects': subjects
    }
    return render(request, 'posts/fille_de_menage.html', context)



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
        # experience = request.POST.get('experience')
        # education = request.POST.get('education')
       


        donnees = Employee.objects.create(email=email, last_name=last_name, 
        first_name=first_name, langage_habituel=langage_habituel, annee_de_naissance=annee_de_naissance,
        numero_employee=numero_employee, emplacement=emplacement ,genre=genre,
        statut=statut, commentaire_sur_savoir_faire=commentaire_sur_savoir_faire)
                        
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
        # moment_pour_vous_contacter = request.POST.get('langage_habituel')



        donnees = Service.objects.create(email=email, last_name=last_name, 
        first_name=first_name, langage_habituel=langage_habituel, ville=ville,
        telephone_principale=telephone_principale,telephone_secondaire=telephone_secondaire,  emplacement=emplacement ,
        service_choisis=service_choisis )
                        
        
        donnees.save()

    return render(request, 'posts/form_adheration.html',{'form':form})













