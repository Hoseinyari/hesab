from django.db import models

# Create your models here

class Transition(models.Model):
    text = models.CharField(max_length=300)
    amount = models.PositiveBigIntegerField()
    date = models.DateTimeField(auto_now=True , editable=False)
    status = [
        ("expose","income")
    ]
    category = models.CharField(max_length=200,choices =status,default='expose')   
    def ___str__(self):
        return self.text
    
