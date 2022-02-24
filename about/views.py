from django.shortcuts import render


from itertools import product
from multiprocessing import context
from urllib import request
from django.shortcuts import render

from product.models import Products,freshSale

# Create your views here.
def about(request):
    return render(request, 'about.html')
