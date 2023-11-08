from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as authlogin,logout as authlogout
from django.views.decorators.cache import  never_cache
# Create your views here.
@never_cache
def login(request):
  if 'user' in request.session:
    return redirect('home')
  
  else:
      if request.method=='POST':
        uname=request.POST.get('username')
        pass1=request.POST.get('password')
        
        user=authenticate(request,username=uname , password=pass1)
        if user is not None:
          authlogin(request,user)
          request.session["user"] = uname
          return redirect('home')
        else:
          return render(request,'login.html',{'error_message': 'Invalid username or password '})
      
  
  return render(request,'login.html')


  # signup value getting 
@never_cache
def Signup(request):
     if 'user' in request.session:
        return redirect('home')
  
     if request.method=="POST":
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        con_pass=request.POST.get('con_password')
        
        #  auth checking
        
        if not (uname and email and pass1 and con_pass):
          return render(request,'signup.html',{'error_message': 'Please fill Required fields...! '})

        elif User.objects.filter(username=uname).exists():
          return render(request,'signup.html',{'error_user': 'Username already exist '})
        
        elif User.objects.filter(email=email).exists():
          return render(request,'signup.html',{'error_email': 'Email already exist '})
        
        elif pass1 != con_pass:
          return render(request,'signup.html',{'error_pass': 'Password mismatch '})
        else:
            user=User.objects.create_user(username=uname,email=email,password=pass1)
            user.save()
            return redirect('login')
     return render(request,'signup.html')


@never_cache
def home(request):
  if "user" in request.session:
    username = request.session["user"]
    
    context1 = {
      "name" : username
    }
    
    return render(request,'home.html',context1)
    
   
  else:
    return redirect('login')
  
@never_cache
def logout(request):
    if 'user' in request.session:
        request.session.flush()
        authlogout(request)
    return redirect('login')