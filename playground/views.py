from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TaggedItem



def say_hello(request):
    # Understanding Queryset cache
    queryset = Product.objects.all()
    # list(queryset)

    return render(request, 'hello.html', {'name': 'Mahfuz Islam',})