from django.shortcuts import render 
from django.http import HttpResponse ,HttpResponseRedirect
from transitions.models import Transition
from django.urls import reverse
# Create your views here. 

def home_view(request): 
    all_transitions = Transition.objects.all().order_by("-date")
    return render(request,'transitions/all_transitions.html',{"all_transitions": all_transitions})

def expose_view(request): 
    exposes = Transition.objects.filter(category='expose').values() 
    return render(request, "transitions/expose.html", {"exposes": list(exposes)}) 

def income_view(request): 
    incomes = Transition.objects.filter(category='income').values()
    return render(request, "transitions/income.html", {"incomes": list(incomes)}) 

def add_transitions(request): 
    if request.method == 'POST': 
        form = request.post
        new_transition= Transition(
            text=form['text'], 
            amount=form['amounth'], 
            date=form['date'], 
            category=form['category'], 
        ) 
        new_transition.save() 
    
    return render(request,'transitions/add_transitions.html')


def submit_transaction(request):
    
    return HttpResponseRedirect(reverse('home_view')) 
