# models.py
from django.db import models

class Shipment(models.Model):
    tracking_id = models.CharField(max_length=20, unique=True)
    trailer = models.CharField(max_length=20)
    trip = models.CharField(max_length=50)
    origin = models.TextField(max_length=100, null=True, blank=True)
    destination = models.TextField(max_length=100 , null=True, blank=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Shipment'
        verbose_name_plural = 'Shipments'

    def __str__(self):
        return f"{self.tracking_id} ({self.origin} → {self.destination})"

