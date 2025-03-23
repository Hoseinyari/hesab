from django.db import models
from accounts.models import Account

# Create your models here

class Transition(models.Model):
    account_id = Account.username
    text = models.CharField(max_length=300)
    amount = models.PositiveBigIntegerField()
    date = models.DateTimeField(auto_now=True , editable=False)
    #وضعیت هایی که فیلد کتگوری می تواند داشته یاشد
    status = [
        ("expose","income")
    ]
    category = models.CharField(max_length=200,choices =status,default='expose')   
    def ___str__(self):
        return self.text
    
