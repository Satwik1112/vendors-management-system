from .models import *
import datetime


def round_up(number: float):
    return float(f"{number:.2f}")


def update_acknowledgement(purchase_order, is_date=False):
    """
    date true => update acknowledgement
    average_response_time = issue date - acknowledgement date then take average each po
    """
    if is_date:
        purchase_order.acknowledgement_date = datetime.datetime.now()
        purchase_order.save()
    # purchase_orders = PurchaseOrder.objects.all()
    # for purchase_order in purchase_orders:
    #     diffrence = purchase_order.issue_date - purchase_order.acknowledgement_date
    average_response_time = 1
    return average_response_time


def calculate_performance_metrics(vendor, purchase_order):
    """
    on_time_delivery_rate = no of po's completed status till delivery_date/ total no. of po's
    quality_rating_avg = (only for completed status) sum of quality ratings from each po / total number of po
    fulfillment_rate = no of completed without issues / total number of po
    """
    completed_orders = PurchaseOrder.objects.filter(status="completed")
    no_po_completed = len(completed_orders)
    total_no_po = len(PurchaseOrder.objects.all())
    sum_quality_ratings = 0
    for orders in completed_orders:
        sum_quality_ratings += int(getattr(orders, "quality_rating"))
    no_po_completed_no_issue = len(PurchaseOrder.objects.filter(status="success"))
    try:
        on_time_delivery_rate = round_up(no_po_completed / total_no_po)
    except ZeroDivisionError:
        print(f"ZeroDivisionError: on_time_delivery_rate = {no_po_completed} / {total_no_po}")
        on_time_delivery_rate = 0
    try:
        quality_rating_avg = round_up(sum_quality_ratings / total_no_po)
    except ZeroDivisionError:
        print(f"ZeroDivisionError: quality_rating_avg = {sum_quality_ratings} / {total_no_po}")
        quality_rating_avg = 0
    try:
        average_response_time = round_up(update_acknowledgement(purchase_order=purchase_order))
    except ZeroDivisionError:
        print(f"ZeroDivisionError: average_response_time")
        average_response_time = 0
    try:
        fulfillment_rate = round_up(no_po_completed_no_issue / total_no_po)
    except ZeroDivisionError:
        print(f"ZeroDivisionError: fulfillment_rate = {no_po_completed_no_issue} / {total_no_po}")
        fulfillment_rate = 0
    history = HistoricalPerformance.objects.create(
        vendor=vendor,
        on_time_delivery_rate=on_time_delivery_rate,
        quality_rating_avg=quality_rating_avg,
        average_response_time=average_response_time,
        fulfillment_rate=fulfillment_rate
    )
    history.save()


def create_code():
    import string
    import random
    alphabets = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return "".join(random.choices(alphabets, k=4))
