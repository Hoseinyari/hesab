from django.shortcuts import render 
from django.http import HttpResponseRedirect
from transitions.models import Transition
from accounts.models import Account
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here. 


#نمایش تمام تراکنش ها در صفحه اصلی
@login_required
def home_view(request): 
    all_transitions = Transition.objects.filter().order_by("-date")
    return render(request,'transitions/home.html',{"all_transitions": list(all_transitions)})
@login_required
#نمایش خرج کرد ها
def expose_view(request): 
    exposes = Transition.objects.filter(category = 'expose')
    return render(request,'transitions/expose.html', {"exposes": list(exposes)}) 
@login_required
#نمایش درامد ها
def income_view(request): 
    incomes = Transition.objects.filter(category = 'income')
    return render(request,'transitions/income.html', {"incomes": list(incomes)}) 
@login_required
#فرم اضافه کردن تراکنش
def add_transitions(request):
    if request.method == "POST":
        # باید ساز و کاری اضافه شود تا تراکنش برای اکانت مئرد نظر ثبت شود
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
