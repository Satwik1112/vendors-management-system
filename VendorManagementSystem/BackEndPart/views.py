from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .utils import *
from .models import *


def welcome(request):
    return HttpResponse("This is API HOST URL")


@api_view(["GET", "POST", "PUT", "DELETE"])
def handle_vendors(request, vendor_id=None):
    if vendor_id:
        try:
            vendor = Vendors.objects.get(id=vendor_id)
        except Vendors.DoesNotExist:
            return Response({"message": f"vendor id '{vendor_id}' is not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            if request.method == "PUT":
                serializer = VendorSerializer(vendor, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
            elif request.method == "DELETE":
                vendor.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == "GET":
        vendor = Vendors.objects.all()
        serializer = VendorSerializer(data=list(vendor.values()), many=True)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    if request.method == "POST":
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return HttpResponse("Data is not valid!", status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)


@api_view(["GET", "POST", "PUT", "DELETE"])
def handle_purchase_order(request, po_id=None):
    if po_id:
        try:
            purchase_order = PurchaseOrder.objects.get(id=po_id)
        except PurchaseOrder.DoesNotExist:
            return Response(data={"message": f"purchase id '{po_id}' is not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            if request.method == "PUT":
                serializer = PurchaseOrderSerializer(purchase_order, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
            if request.method == "DELETE":
                purchase_order.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == "GET":
        vendor_code = request.data.get("vendor_code")
        if vendor_code:
            vendor = Vendors.objects.filter(vendor_code=vendor_code)
            purchase_order = PurchaseOrder.objects.filter(vendor=vendor)
        else:
            purchase_order = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(data=dict(purchase_order.values()))
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    if request.method == "POST":
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response({}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)


@api_view(["GET"])
def vendor_performance(request, vendor_id):
    if request.method == "GET":
        try:
            vendor = Vendors.objects.get(gameID=vendor_id)
        except Vendors.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = VendorPerformanceSerializer(vendor)
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(["GET"])
def handle_acknowledgment(request, po_id=None):
    if request.method == "GET":
        try:
            purchase_order = PurchaseOrder.objects.get(id=po_id)
        except PurchaseOrder.DoesNotExist:
            return Response({"message": f"purchase id '{po_id}' not found for acknowledgment"},
                            status=status.HTTP_404_NOT_FOUND)
        else:
            return JsonResponse({"status": bool(update_acknowledgement(purchase_order=purchase_order, is_date=True))})
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
