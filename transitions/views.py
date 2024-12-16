from datetime import date
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from transitions.models import *

# Create your views here.

def home_view (request):

    transitions=transitions.objects.all()

    return render()

def expose_view(request):

    exposes = Transitions.objects.filter(name='expose').values()


    return render()

def income_view(request):
    incomes = Transitions.objects.filter(name='income').values()

    return render()

def add_transitions(request):

    transitions = Transitions (

        text = request.post["text"],
        amounth = request.post["amounth"],
        date = request.post["date"],
        category = request.post["category"],
    )

    transitions.save()
        
    return render()
