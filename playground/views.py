from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from store.models import Product, Order, OrderItem



def say_hello(request):
    # Selecting related object
    queryset = Product.objects.select_related('collection').all() # works for foreignkey / oneToOneField
    queryset = Product.objects.prefetch_related('promotion').all() # works for manyToManyField / reverse foreignkey

    # practice (get the last 5 orders with their customer and items (including product))
    queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-id')[:5]




    return render(request, 'hello.html', {'name': 'Mahfuz Islam', 'orders': list(queryset)})