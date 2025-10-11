from django.shortcuts import render
from store.models import Product, Collection, Order, OrderItem
from django.db import connection


def say_hello(request):
    # Executing Raw SQL Queries
    queryset = Product.objects.raw('SELECT * FROM store_product')
    # here we can't access like queryset.filter or queryset.object etc.. not possible for raw queries

    # sometimes we want execute queries that don't map to our model objects. in those cases we can access our database 
    # and bypass the model layer
    cursor = connection.cursor()
    cursor.execute('write any query here')
    cursor.close()

    # best way using (with statement)
    with connection.cursor() as cursor:
        cursor.execute('write any query here')
        # we don't need to close here!

    # we also have another method here to execute stored_procedure
    with connection.cursor() as cursor:
        cursor.callproc('get_customers', [1, 2, 3, 'a'])
        # we don't need to close here!

    return render(request, 'hello.html', {'name': 'Mahfuz Islam', 'results': list(queryset)})