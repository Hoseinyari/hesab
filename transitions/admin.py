from django.contrib import admin
from .models import Transitions,Category

# Register your models here.

class CategoryAdmin (admin.ModelAdmin):
    model = Category
    list_display = ["name"]
    # ,"start_time","end_time"


admin.site.register(Category,CategoryAdmin)


class TransitionsAdmin (admin.ModelAdmin):
    model = Transitions
    list_display = ["id","text","amounth","date","category"]

admin.site.register(Transitions,TransitionsAdmin)
