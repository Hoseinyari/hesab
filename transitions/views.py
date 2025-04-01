from django.shortcuts import render 
from django.http import HttpResponseRedirect
from transitions.models import Transition
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here. 

#نمایش تمام تراکنش ها در صفحه اصلی
@login_required
def home_view(request): 
    all_transitions = Transition.objects.filter(user=request.user).order_by("-date")
    return render(request,'transitions/home.html',{"all_transitions": list(all_transitions)})
@login_required
#نمایش خرج کرد ها
def expose_view(request): 
    exposes = Transition.objects.filter(user=request.user,category = 'expose')
    return render(request,'transitions/expose.html', {"exposes": list(exposes)}) 
@login_required
#نمایش درامد ها
def income_view(request): 
    incomes = Transition.objects.filter(user=request.user,category = 'income')
    return render(request,'transitions/income.html', {"incomes": list(incomes)}) 
@login_required
#فرم اضافه کردن تراکنش
def add_transitions(request):
    if request.method == "POST":
        form = request.POST
        new_transition= Transition(
            user = request.user,
            text=form['text'], 
            amount=form['amount'], 
            date=form['date'], 
            category=form['category'], 
        ) 
        #save data in database and then redirect you to all transitions
        new_transition.save() 
        return HttpResponseRedirect(reverse("home_view"))
    else:

        return render(request,'transitions/add_transitions.html')
