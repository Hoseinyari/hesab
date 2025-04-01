from django.db import models
from accounts.models import Account

# Create your models here

class Transition(models.Model):
    user = models. ForeignKey(Account, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    amount = models.PositiveBigIntegerField()
    date = models.DateTimeField(auto_now=True , editable=False)
    #options for your transitions status ( which category is your transition ?? )
    status = [
        ("expose","income")
    ]
    category = models.CharField(max_length=200,choices =status,default='expose')   
    def ___str__(self):
        return self.text
    
