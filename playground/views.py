from django.shortcuts import render
from django.db.models.aggregates import Avg, Max, Min, Count
from store.models import Product



def say_hello(request):
    # Aggregating objects
    result = Product.objects.filter(collection__id=1).aggregate(count=Count('id'), min_price=Min('unit_price'))


    return render(request, 'hello.html', {'name': 'Mahfuz Islam', 'result': result})