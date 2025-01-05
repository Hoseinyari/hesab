from django.db import models

# Create your models here

class Category(models.Model):
    name= models.CharField(max_length=200)
    def ___str__(self):
        return self.title
    
class Transitions(models.Model):
    text = models.CharField(max_length=300)
    amounth = models.PositiveBigIntegerField()
    date = models.DateTimeField(auto_now=True , editable=False)
    category = models.ForeignKey(Category , on_delete=models.PROTECT)
    def ___str__(self):
        return self.title
    

# class Sort(models.Model):
#     incomes = Category.objects.filter(name='Income').values()
#     Exposes = Category.objects.filter(name='Expose').values()