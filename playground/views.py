from django.shortcuts import render
from store.models import Product, Collection, Order, OrderItem
from django.db import transaction


def say_hello(request):
    # Executing Raw SQL Queries
    queryset = Product.objects.raw('SELECT * FROM store_product')
    # here we can't access like queryset.filter or queryset.object etc.. not possible for raw queries



    return render(request, 'hello.html', {'name': 'Mahfuz Islam', 'results': list(queryset)})