from django.shortcuts import render,redirect
from . models import Login
from django.contrib.auth.models import auth
from django.http import HttpResponse

# Create your views here.
def register_page(request):
    if request.method =="POST":
        euser_name = request.POST['user_name']
        efirst_name = request.POST['first_name']
        elast_name = request.POST['last_name']
        eemail = request.POST['email']
        epassword = request.POST['password']
        econfrom_password = request.POST['confrom_password']
        a = Login(user_name=euser_name,first_name=efirst_name,last_name=elast_name,email=eemail,password=epassword,confrom_password=econfrom_password)
        a.save()
        if econfrom_password != econfrom_password:
            return HttpResponse("INCRCT PASSWORD")
        else:
          

            return redirect('login')
    print("Success Register")

    return render(request,'register.html')


def login_page(request):
    if request.method == "POST":
        buser_name = request.POST['user_name']
        bpassword = request.POST['password']
        log=Login.objects.all()
        log1= None
        for i in log:
            if(i.user_name,i.password)==(buser_name,bpassword):
                log1=i.user_name
                break
        if log1 is not None:
            print("Success Login")
            return redirect('home')
        else:
            return HttpResponse("INVAlID USERNAME OR PASSWOED!!!")
        
            
    return render(request,'login.html')





def home_page(request):
    if request.method=='POST':
        return redirect('login')
    return render(request,'home.html')