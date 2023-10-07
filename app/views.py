from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Customer
from django.views.decorators.cache import never_cache

# Create your views here.
@never_cache
def index(request):
    if request.user.is_authenticated:
        return render(request,'index.html')
    return redirect(handlelogin)

def root_view(request):
    # Your view logic here
    return render(request, 'index.html')  # Replace with your desired template


def search(request):
    query = request.GET.get('query', '')
    users = Customer.objects.filter(name__icontains=query)
    return render(request,'search.html',{'users':users})

def about(request):
    if request.method=="POST":
        uname= request.POST.get("name")
        uemail=request.POST.get("email")
        phone=request.POST.get("phone")
        desc=request.POST.get("desc")
        query = Customer(name=uname,email=uemail,phoneNumber=phone,description=desc)
        query.save()
        messages.info(request,"Thanks for contacting us, See you soon")
    return render(request,'about.html')

def info(request):
    return render(request,'info.html')
@never_cache
def handlelogin(request):
    if request.user.is_authenticated:
        return redirect(index)
    
    if request.method == 'POST':
        uname = request.POST.get("username")
        pass1 = request.POST.get("pass1")
        myuser=authenticate(username=uname,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Logged In Successfully")
            return redirect(index)
        else:
            messages.error(request,"Invalid request")
            return redirect('/login')

    return render(request,'login.html')

@never_cache
def handlesignup(request):
    if request.user.is_authenticated:
        return redirect(index)
    if request.method == 'POST':
        uname = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("pass1")
        confirmpassword = request.POST.get("pass2")
        # print(username, email, password, confirmpassword)
       
        if password != confirmpassword:
            messages.warning(request,"Password is incorrect")
            return redirect('/signup')
        try:
            if User.objects.get(username=uname):
                messages.info(request,"Username is taken")
                return redirect('/signup')
        except:
            pass
        try:
            if User.objects.get(email=email):
                messages.info(request,"Email is taken")
                return redirect('/signup')
        except:
            pass
        
        
        myuser = User.objects.create_user(uname,email)
        myuser.set_password(password)
        myuser.save()
        messages.success(request,"SignUp Successfull. Please Login!")
        return redirect('/login')
    
    return render(request,'signup.html') 
@never_cache
def handlelogout(request):
    if request.user.is_authenticated:
        
        logout(request)
    messages.info(request,"Logout success")
    return redirect('/login')
