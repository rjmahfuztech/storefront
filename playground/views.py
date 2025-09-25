from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from store.models import Product, OrderItem



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
    # products = Product.objects.filter(inventory=F('collection__id'))

    # Products: Sorting products using order_by() and we can reverse it using reverse()
    # products = Product.objects.order_by('unit_price', '-title').reverse()
    # products = Product.objects.filter(collection__id=1).order_by('unit_price')
    # product = Product.objects.order_by('unit_price')[0] # it's give the 1st sorted object not queryset
    # similar
    # product = Product.objects.earliest('unit_price') # sort in ascending and return the first object
    # product = Product.objects.latest('unit_price') # sort in descending and return the first object

    # Products: Getting product using limit (array [] slicing)
    products = Product.objects.all()[5:10]

    # Selecting fields to query
    products = Product.objects.values_list('id', 'title', 'collection__title')

    # practice
    queryset = OrderItem.objects.values('product_id').distinct()
    products = Product.objects.filter(id__in=queryset).order_by('title')


    return render(request, 'hello.html', {'name': 'Mahfuz Islam', 'products': list(products)})