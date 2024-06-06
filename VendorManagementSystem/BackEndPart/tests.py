from django.test import TestCase

"""
'vendors/', handle_vendors
    GET:
    {
    "name":"vendor1",
    "contact_details":"12345",
    "address":"India"
    }
'vendors/<int:vendor_id>/', handle_vendors

'vendors/<int:vendor_id>/performance', vendor_performance

'purchase_order/', handle_purchase_order
    {
    "order_date": "03/05/2024 10:30:20.000000-08:00", 
    "delivery_date": "04/05/2024 10:30:20.000000-08:00",
    "issue_date": "06/05/2024 10:30:20.000000-08:00", 
    "items": [1,2,3,4],
    "quantity": 4,
    "status": "completed",
    "vendor": 1
    }
'purchase_order/<int:po_id>/', handle_purchase_order

'purchase_order/<int:po_id>/acknowledge', handle_acknowledgmen

"""