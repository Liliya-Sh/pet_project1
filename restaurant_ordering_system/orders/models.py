from django.db import models

class Order(models.Model):
    """Заказ, который сделал клиент"""
    name = models.CharField(max_length=50, null=True)
    order = models.CharField(max_length=50, null=True)
    ready_to_delivery = models.CharField(max_length=50, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Create your models here.
