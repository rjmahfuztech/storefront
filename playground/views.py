from django.shortcuts import render
from django.db.models import F, Value, Func, Count, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from store.models import Product, Customer



def say_hello(request):
    # Calling database functions
    queryset = Customer.objects.annotate(
        # CONCAT
        full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT')
    )

    # Another way to do the same concatenation in short way
    queryset = Customer.objects.annotate(
        # CONCAT
        full_name=Concat('first_name', Value(' '), 'last_name')
    )

    # Grouping data
    # Counting the order for each customer and store it in a new field
    queryset = Customer.objects.annotate(
        order_count=Count('order')
    )

    # ExpressionWrapper
    discount_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    queryset = Product.objects.annotate(discount_price=discount_price)

    return render(request, 'hello.html', {'name': 'Mahfuz Islam', 'customers': list(queryset)})