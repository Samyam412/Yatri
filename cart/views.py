import json
from django.http import JsonResponse
from django.shortcuts import render
from cart.models import Order, OrderedProducts

from product.models import Products

# Create your views here.

def updateCart(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user
    product = Products.objects.get(id=productId)
    order, created = Order.objects.get_or_create(userData = customer,  complete=False)

    orderedproducts,created = OrderedProducts.objects.get_or_create(order=order,product=product)

    if action == 'add':
        orderedproducts.quantity = (orderedproducts.quantity + 1)
    elif action == 'remove':
        orderedproducts.quantity = (orderedproducts.quantity - 1)
    elif action == 'addWithQty':
        orderedproducts.quantity = (orderedproducts.quantity + int(qty))
    elif action == 'deleteItem':
        orderedproducts.quantity = 0
    orderedproducts.save()


    if orderedproducts.quantity <=0:
        orderedproducts.delete()

    # return redirect ('index')

    return JsonResponse('HREER', safe=False)

def cart(request):
    

    user_data= request.user
    order, created = Order.objects.get_or_create(userData= user_data, complete=False)
    items = order.orderedproducts_set.all()
    data={
        'items':items,
        'order':order,

    }
    return render(request,'cart.html',data)

