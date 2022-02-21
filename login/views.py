from pickle import NONE
from django.shortcuts import redirect, render
from django.contrib.auth import login as loginVerification, logout, authenticate, get_user_model;
# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect ('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username, password=password)

            if username and password !="":
                if user is not None:
                    loginVerification(request,user)
                    return redirect('index')
                else:
                    print('Username or password is incorrect')
            else:
                print('Enter Username or password is incorrect')

    return render(request, 'login.html')

def signout(request):
    logout(request)
    return redirect('index')

 