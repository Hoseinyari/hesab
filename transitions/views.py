from django.shortcuts import render 
from django.http import HttpResponse ,HttpResponseRedirect
from transitions.models import Transition
from django.urls import reverse
# Create your views here. 


# def home_view(request): 
#     all_transitions = Transition.objects.all().order_by("-date")
#     return render(request,'transitions/all_transitions.html',{"all_transitions": list(all_transitions)})

def home_view(request): 
    all_transitions = Transition.objects.all().order_by("-date")
    return render(request,'transitions/home.html',{"all_transitions": list(all_transitions)})


def expose_view(request): 
    exposes = Transition.objects.filter(category_id = 1)
    return render(request,'transitions/expose.html', {"exposes": list(exposes)}) 

def income_view(request): 
    incomes = Transition.objects.filter(category_id = 2)
    return render(request,'transitions/income.html', {"incomes": list(incomes)}) 

def add_transitions(request): 
    if request.method == 'GET': 
        form = request.POST
        new_transition= Transition(
            text=form['text'], 
            amounth=form['amounth'], 
            date=form['date'], 
            category=form['category'], 
        ) 
        new_transition.save() 
    
        return render(request,'transitions/add_transitions.html')
    else:

        return render(request,'transitions/home.html')


def submit_transaction(request,new_transition):

    new_transition.save() 
    
    return HttpResponseRedirect(reverse('home_view')) 