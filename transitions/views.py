from datetime import date
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from transitions.models import Transitions,Category

# Create your views here.

def home_view (request):

    all_transitions=Transitions.objects.all()

    return render(request,'transitions/all_transitions.html',{"all_transitions":list(all_transitions)})

def expose_view(request):

    exposes = Transitions.objects.filter(category='expose').values()


    return render(request,'transitions/expose.html',{"exposes":list(exposes)})

def income_view(request):
    
    incomes = Transitions.objects.filter(category='income').values()

    return render(request,'transitions/incime.html',{"incomes":list(incomes)})

def add_transitions(request):

    transitions = Transitions (

        text = request.post["text"],
        amounth = request.post["amounth"],
        date = request.post["date"],
        category = request.post["category"],
    )

    transitions.save()
        
    return render(request,'transitions/add_transitions.html',{"transitions":list(transitions)})
