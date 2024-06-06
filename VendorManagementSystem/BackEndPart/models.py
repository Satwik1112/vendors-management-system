import datetime
from .utils import create_code
from django.db import models


class Vendors(models.Model):
    name = models.CharField(max_length=30)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(unique=True, max_length=35, default=create_code)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    def __str__(self):
        return f"{self.vendor_code}"


class PurchaseOrder(models.Model):
    po_code = models.CharField(unique=True, max_length=8, default=create_code)
    vendor = models.ForeignKey(Vendors, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=10)
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateTimeField()
    acknowledgement_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.__class__}{self.po_code}"


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendors, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.datetime.now())
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.__class__}{self.date}"
