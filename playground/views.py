from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from store.models import Product, OrderItem



def say_hello(request):
    # Deferring Fields
    queryset = Product.objects.only('id', 'title') # load only id and title from DB
    queryset = Product.objects.defer('description') # load all data but not description

    # so only() load the data we want and later if we want other field then it will query again for load that data
    # and defer() do not load the data that we select and if we need it later then it will query again for load that data
    


    return render(request, 'hello.html', {'name': 'Mahfuz Islam', 'products': list(queryset)})