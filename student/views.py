from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
# Create your views here.
from resume import views

def homepage(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('student:register')
            elif User.objects.filter(email=email).exists() :
                messages.info(request, 'email Taken')
                return redirect('student:register')
            elif '1RV' in username:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                messages.info(request, 'successfully created account')
                return redirect('student:login')
            elif 'RVCE' in username:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                messages.info(request, 'successfully created account')
                return redirect('student:login')    

            else:
                messages.info(request, 'Enter your valid Username')
                return redirect('student:register')
               
        else:
            messages.info(request, 'Password is not matching') 
            return redirect('student:register')
        return redirect('/')
    else:    
     return render(request, 'register.html')
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        print(username)
        if user is not None:
            auth.login(request, user)
            print('user login')
            if 'RVCE' in username:
                return redirect('resume:list')
            elif '1RV' in username:
                 return redirect('resume:profile')
            else:
                messages.info(request, 'Enter valid username or password')
                return redirect('student:login')      
        else:
             messages.info(request, 'Enter valid username or password')
             return redirect('student:login')
    else:
        return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
