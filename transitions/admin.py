from django.contrib import admin
from .models import Transition,Category

# Register your models here.

class CategoryAdmin (admin.ModelAdmin):
    model = Category
    list_display = ["name"]

admin.site.register(Category,CategoryAdmin)


class TransitionAdmin (admin.ModelAdmin):
    model = Transition
    list_display = ["id","text","amount","date","category"]

admin.site.register(Transition,TransitionAdmin)
