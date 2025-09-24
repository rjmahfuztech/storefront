from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from store.models import Product



def say_hello(request):
    # Complex lookups Using Q objects

    # Products: inventory < 20 AND price < 500
    # products = Product.objects.filter(inventory__lt=20, unit_price__lt=500)
    # another way for same filter
    # products = Product.objects.filter(inventory__lt=20).filter(unit_price__lt=500)

    # Products: inventory < 20 OR price < 500
    # products = Product.objects.filter(Q(inventory__lt=20) | Q(unit_price__lt=500))

    # Products: inventory < 20 & NOT (~) price < 500
    # products = Product.objects.filter(Q(inventory__lt=20) | ~Q(unit_price__lt=500))

    # Products: Referencing or filtering 2 fields in the same model using (F) object
    # products = Product.objects.filter(inventory=F('unit_price'))

    # Products: Using F object we can also reference a field in a related table
    products = Product.objects.filter(inventory=F('collection__id'))



    return render(request, 'hello.html', {'name': 'Mahfuz Islam', 'products': list(products)})