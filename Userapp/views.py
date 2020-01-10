from django.shortcuts import render,redirect
from Userapp.models import UserReg
from Userapp.forms import UserForm
from Firstapp.models import ITJobs,MECHJobs,CIVILJobs
from Userapp.decorator import user_login


from django.http import HttpResponse
from django.contrib import messages
# Create your views here.

# user first welcome page
def welcome_user(request):
    return render(request,'Welcome_user.html')

#dashboard page
def userdashboard(request):
    return render(request,'dashboard_user.html')

# User Registration page
def userregister(request):
    if request.method=="POST":
        ureg=UserForm(request.POST,request.FILES)
        if ureg.is_valid():
            ureg.save()
        return redirect('/userapp/user_login/')
    ureg=UserForm()   
    return render(request,'userreg.html',{'ureg':ureg})

#User login page
def userlogin(request):
    if request.method=='POST':
        Username=request.POST['txtuname']
        Password=request.POST["txtpasswd"]
        try:
            user=UserReg.objects.get(Username=Username,Password=Password)
            if (user):
                request.session['user'] = user.Username
                print(request.session.get('user'))
                return render(request,'dashboard_user.html')
            else:
                messages.error(request,'please enter valid username and password')
                return redirect('/userapp/user_login/')  
        except Exception :
            messages.error(request,'please enter valid username and password')
            return redirect('/userapp/user_login/')  
    return render(request,'loginuser.html')

#User IT JOB show
@user_login
def it_showuser(request):
    obj=ITJobs.objects.all()
    return render(request,'it_show_user.html',{'obj':obj})

#User Mechanical Job show
def mech_showuser(request):
    obj=MECHJobs.objects.all()
    return render(request,'mech_show_user.html',{'obj':obj})
        
#User civil job show
def civil_showuser(request):
    obj=CIVILJobs.objects.all()
    return render(request,'civil_show_user.html',{'obj':obj})


