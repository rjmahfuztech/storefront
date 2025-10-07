from django.shortcuts import render
from store.models import Product, Collection



def say_hello(request):
    # Creating Objects
    collection = Collection(title='video games', featured_product_id=1)

    # another way
    collection = Collection()
    collection.title = 'Video Games'
    collection.featured_product = Product(pk=1)
    collection.save()

    # another way using create method
    Collection.objects.create(title='Video Games', featured_product_id=1)

    return render(request, 'hello.html', {'name': 'Mahfuz Islam',})