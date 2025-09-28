from django.shortcuts import render
from django.db.models import F, Value
from store.models import Product, Customer



def say_hello(request):
    # Annotating objects - It adds a new field on each object
    queryset = Customer.objects.annotate(new_id=F('id') + 1)

    return render(request, 'hello.html', {'name': 'Mahfuz Islam', 'customers': queryset})