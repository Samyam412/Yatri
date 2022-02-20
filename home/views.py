from itertools import product
from multiprocessing import context
from urllib import request
from django.shortcuts import render

from product.models import Products,freshSale,Popualar

# Create your views here.
def index(request):
    
    popualar = Popualar.objects.all()
    freshsale = freshSale.objects.all()
    context={
        'freshsale':freshsale,
        'popular':popualar
    }
    return render(request, 'index.html',context)
