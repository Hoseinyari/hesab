from datetime import date 
from django.shortcuts import render, redirect 
from django.http import HttpResponse 
from transitions.models import Transition

# Create your views here. 

def home_view(request): 
    all_transitions = Transition.objects.all() 
    return render(request,"transitions/all_transitions.html",{"all_transitions": all_transitions})

def expose_view(request): 
    exposes = Transition.objects.filter(category='expose').values() 
    return render(request, "transitions/expose.html", {"exposes": list(exposes)}) 

def income_view(request): 
    incomes = Transition.objects.filter(category='income').values() 
    return render(request, "transitions/income.html", {"incomes": list(incomes)}) 

def add_transitions(request): 
    if request.method == 'POST': 
        transition= Transition(
            text=request.POST["text"], 
            amount=request.POST["amount"], 
            date=request.POST["date"], 
            category=request.POST["category"], 
        ) 
        transition.save() 
        return redirect('home_view') 

    return render(request, 'transitions/add_transitions.html')
