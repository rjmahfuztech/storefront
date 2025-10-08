from django.shortcuts import render
from store.models import Product, Collection



def say_hello(request):
    # updating objects
    collection = Collection.objects.get(pk=11)
    collection.title = 'Video Games'
    collection.featured_product = None
    collection.save()

    # another way
    Collection.objects.filter(pk=11).update(featured_product=None)


    # deleting objects
    
    # single delete
    collection = Collection(pk=13)
    # collection.delete()

    # multiple delete
    Collection.objects.filter(id__gt=11).delete()



    return render(request, 'hello.html', {'name': 'Mahfuz Islam',})