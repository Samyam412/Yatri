from pickle import NONE
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate, get_user_model
from register.forms import CreateRegisterForm


# Create your views here.
def register(request):
    current_user = request.user
    if request.user.is_authenticated:
        return redirect ('index')
    else:
        form = CreateRegisterForm()

        if request.method == 'POST':
            print(request.POST)
            print("Got data")
            form = CreateRegisterForm(request.POST)
            if form.is_valid():
                print("form valid")
                form.save()
                print("form saved")
                return redirect('login')
            else:
                pass



        data ={
            'form':form,
        }

    return render(request,'signup.html',data)


 