from rest_framework import serializers
from .models import *
from .utils import create_code


class VendorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendors
        fields = "__all__"


class PurchaseOrderSerializer(serializers.ModelSerializer):
    order_date = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S")
    delivery_date = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S")
    issue_date = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S")
    acknowledgement_date = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S")

    class Meta:
        model = PurchaseOrder
        fields = "__all__"


class VendorPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendors
        fields = ["on_time_delivery_rate", "quality_rating_avg", "average_response_time", "fulfillment_rate"]
