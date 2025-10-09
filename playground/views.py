from django.shortcuts import render
from store.models import Product, Collection, Order, OrderItem
from django.db import transaction


def say_hello(request):
    # Transactions
    with transaction.atomic():
        order = Order()
        order.customer_id = 1
        order.save()

        item = OrderItem()
        item.order = order
        item.product_id = -1
        item.quantity = 1
        item.unit_price = 10
        item.save()


    return render(request, 'hello.html', {'name': 'Mahfuz Islam',})