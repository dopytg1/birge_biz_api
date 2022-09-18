from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class VerifiedDeliverer(models.Model):
    phone_number = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    telegramId = models.CharField(max_length=64, default="")
    whoAdded = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    pub_date = models.DateTimeField('date published')
    status = models.IntegerField(default=0)
