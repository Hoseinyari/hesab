from django.contrib import admin
from .models import Transition

# Register your models here.

class TransitionAdmin (admin.ModelAdmin):
    model = Transition
    list_display = ["id","text","amount","date","category"]

admin.site.register(Transition,TransitionAdmin)
