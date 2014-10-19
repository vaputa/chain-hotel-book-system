from django.db import models

from common.customer.models import Customer

class Order(models.Model):
    order_id = models.AutoField(primary_key = True)
    order_time = models.DateTimeField(auto_now = True)
    customer = models.ForeignKey(Customer)
    price = models.IntegerField()
    status = models.IntegerField()
    