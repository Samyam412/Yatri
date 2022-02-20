from django.shortcuts import render

from product.models import Products

# Create your views here.
def displayshop(request):
    productList = Products.objects.all()

    context={
        'productList':productList,
    }
    return render(request,'shop.html',context)
