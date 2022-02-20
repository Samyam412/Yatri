from itertools import product
from multiprocessing import context
from urllib import request
from django.shortcuts import render

from product.models import Products,freshSale

# Create your views here.
def index(request):
    

    freshsale = freshSale.objects.all()
    context={
        'freshsale':freshsale
    }
    return render(request, 'index.html',context)
