from django.shortcuts import render 
from django.http import HttpResponseRedirect
from transitions.models import Transition
from django.urls import reverse
# Create your views here. 


#نمایش تمام تراکنش ها در صفحه اصلی
def home_view(request): 
    all_transitions = Transition.objects.all().order_by("-date")
    return render(request,'transitions/home.html',{"all_transitions": list(all_transitions)})

#نمایش خرج کرد ها
def expose_view(request): 
    exposes = Transition.objects.filter(category = 'expose')
    return render(request,'transitions/expose.html', {"exposes": list(exposes)}) 
#نمایش درامد ها
def income_view(request): 
    incomes = Transition.objects.filter(category = 'income')
    return render(request,'transitions/income.html', {"incomes": list(incomes)}) 
#فرم اضافه کردن تراکنش
def add_transitions(request):
    if request.method == "POST":
        form = request.POST

        new_transition= Transition(
            text=form['text'], 
            amount=form['amount'], 
            date=form['date'], 
            category=form['category'], 
        ) 
        #ذخیره اطلاعات در دیتابیس
        new_transition.save() 
        #بازگشت به صفحه اصلی پس از ثبت تراکنش
        return HttpResponseRedirect(reverse("home_view"))
    else:

        return render(request,'transitions/add_transitions.html')
