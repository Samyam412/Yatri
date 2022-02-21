from django.db import models
from django.conf import settings

# Create your models here.
class checkoutDetail(models.Model):
    order_id = models.AutoField(primary_key=True)
    user=  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")