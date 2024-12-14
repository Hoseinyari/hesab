from django.contrib import admin
from .models import Transitions,Category
# Register your models here.

class TransitionsAdmin (admin.ModelAdmin):
    model = Transitions
    list_display = ["id","text","amounth","date","category"]

admin.site.register(Transitions,TransitionsAdmin)


admin.site.register(Category)
