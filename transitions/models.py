from django.db import models

# Create your models here

class Category(models.Model):
    name  = [
        ('expose','خرج'),
        ('income','درامد')
    ]
    statuse=models.CharField(max_length=200,choices = name)

    # def ___str__(self):
    #     return self.title
    
class Transition(models.Model):
    text = models.CharField(max_length=300)
    amounth = models.PositiveBigIntegerField()
    date = models.DateTimeField(auto_now=True , editable=False)
    category = models.ForeignKey(Category , on_delete=models.PROTECT)
    def ___str__(self):
        return self.title
    

# class Sort(models.Model):
#     incomes = Category.objects.filter(name='Income').values()
#     Exposes = Category.objects.filter(name='Expose').values()