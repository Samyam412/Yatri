from django.shortcuts import redirect, render
from checkout.models import checkoutDetail
from cart.models import Order, OrderedProducts

from product.models import Products

def checkoutView(request):
    customer = request.user
    order, created = Order.objects.get_or_create(userData= customer, complete=False)
    items = order.orderedproducts_set.all()
    print(items)
    print(order.id)
    data={
        'items':items,
        'order':order,
    }


    return render(request,'checkout.html',data)

def savecheckout(request):
    if request.method == 'POST':
        orderid = request.POST.get('o_id')
        # orderid = Order.objects.get(id=orderid)
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        print(full_name)
        print(email)
        print(phone)
        print(address)

        saveData = checkoutDetail(user=request.user,order_id=orderid,name=full_name, phone=phone, email=email,address=address)
        saveData.save()
        orderid.complete=True
        orderid.save()

    return redirect('index')