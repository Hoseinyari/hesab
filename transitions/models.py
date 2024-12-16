from django.db import models
#from django.utils import timezone

# Create your models here

class Category(models.Model):
    names = models.CharField(max_length=200)
    
    start_time = models.DateField()
    end_time = models.DateField()

class Transitions(models.Model):
    text = models.CharField(max_length=300)
    amounth = models.PositiveBigIntegerField()
    date = models.DateTimeField(auto_now=True , editable=False)
    category = models.ForeignKey(Category , on_delete=models.PROTECT)
    def __unicode__(self):
        return '{}-{}'.format(self.date , self.amounth)
    

# class Sort(models.Model):
#     incomes = Category.objects.filter(name='Income').values()
#     Exposes = Category.objects.filter(name='Expose').values()