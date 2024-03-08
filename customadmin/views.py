from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from. models import *
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.

@never_cache
def adminlogin(request):

    
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)
        if user is not None:
            if user and user.is_superuser:
                login(request,user)
                return redirect('dashboard')
        else:
            messages.error(request,'Invalid User')
    return render(request,'adminlogin.html')   
# @login_required(login_url='adminlogin/')
def adminlogout(request):

    logout(request)

    return redirect('adminlogin')

# @login_required(login_url='adminlogin/')
def dashboard(request):
    if request.user.is_superuser:

        users = User.objects.all()

        query = request.GET.get('q')
        
        if query:
            users = User.objects.filter(
                Q(username__icontains=query) |
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(email__icontains=query)
            )

        context = {
            'users': users,
            'search_query': query
        }
        return render(request,'customadmin.html',context)
    return redirect('adminlogin')

# add user

def add(request):
    if request.method == 'POST':
        first_name = request.POST['first_name'].strip()
        last_name = request.POST['last_name'].strip()
        username = request.POST['username'].strip()
        email = request.POST['email'].strip()

        if not first_name or not last_name or not username or not email:
            messages.error(request,'All the fields are required')
            return redirect('dashboard')
        
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username already exist. Try another one')
            return redirect('dashboard')
        elif User.objects.filter(email=email).exists():
             messages.info(request,'Email already exist. Try another one')
             return redirect('dashboard')
        else:
            new_user = User.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email
            )
            new_user.save()
            return redirect('dashboard')

    return render(request,'customadmin.html')

# edit user

def edit(request):

    users = User.objects.all()

    context = {
        'user':user
    }
    return render(request,'customadmin.html',context)

# update user

def update(request,id):

    if request.method =='POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']

        users = User(
            
            id = id,
            first_name= first_name,
            last_name= last_name,
            username= username,
            email= email
        )
        users.save()
        return redirect('dashboard')

    return render(request,'customadmin.html')

# delete user

def delete(request,id):

    users = User.objects.filter(id = id).delete()

    context = {
        'users':users
    }
    return redirect('dashboard')    