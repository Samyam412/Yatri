from django.shortcuts import render

from product.models import Products

# Create your views here.
def productview(request,p_id):
    productList = Products.objects.all()

    context={
        'productList':productList,
    }
    return render(request,'prodView.html',context)