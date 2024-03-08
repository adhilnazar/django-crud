from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def log_in(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('log_in')
    else:
        return render(request, 'login.html')
    
def regi_ster(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        first_name = request.POST['first_name'].strip()
        last_name = request.POST['last_name'].strip()
        username = request.POST['username'].strip()
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email'].strip()

        if not first_name or not last_name or not email or not password1 or not password2:
            messages.error(request, 'all the fields are required')
            return redirect('regi_ster')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username is taken')
                return redirect('regi_ster')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already in use')
                return redirect('regi_ster')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('created')
                messages.success(request,"You have successfully signed in")
                return redirect('log_in')
        else:
            messages.info(request, "password didn't match")
            return redirect('regi_ster')
             
    else:       
        return render(request, 'signup.html')

@login_required(login_url='/')    
def home(request):
    if not request.user:
        logout(request)
        messages.error(request,"Register Again")
        return redirect('regi_ster')
    
    return render(request,'home.html')

@login_required(login_url='/')
def log_out(request):
    auth.logout(request)
    return redirect('log_in')