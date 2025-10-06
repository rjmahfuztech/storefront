from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TaggedItem



def say_hello(request):
    # Understanding Queryset cache
    queryset = Product.objects.all()
    list(queryset) # first time django run the query on entire Product and save the cache
    list(queryset) # now it's not run the queryset again. Just get from the cache

    # Caching happen only if they evaluate the entire queryset first
    # example (right way)
    list(queryset)
    queryset[0]

    # but first if we try to access only few data and again try to get all data then it run 2 queries (not good approach)
    queryset[0] # not running entire queryset
    list(queryset)

    return render(request, 'hello.html', {'name': 'Mahfuz Islam',})