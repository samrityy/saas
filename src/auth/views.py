from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from django.contrib.auth import get_user_model
User=get_user_model()
# Create your views here.
def login_view(request):
    if(request.method == "POST"):
        username= request.POST.get("username") 
        password = request.POST.get("password") 
        if all([username,password]):
            user=authenticate(request,username=username,password=password)
            print('user',user)
            if user is not None:
                login (request, user)
                print("login here!")
                return redirect("/")
    return render(request,"auth/login.html",{})    

def register_view(request):
    if request.method=="POST":
        username=request.POST.get("username")or None
        email= request.POST.get("email") or None
        password=request.POST.get("password") or None
        
        #Django Forms
        # user_exist_qs=User.objects.filter(username__iexact=username).exist
        # email_exist_qs=User.objects.filter(email__iexact=email).exist
        User.objects.create_user(username,email=email,password=password)
    return render(request, "auth/register.html", {})
