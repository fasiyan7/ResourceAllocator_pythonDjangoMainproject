from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from oneteamapp.EmailBackEnd import EmailBackEnd
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from oneteamapp.models import CustomUser



   
# Create your views here.
def LOGIN(request):
	return render(request,'loginboth.html')
def Test(request):
    return render(request,'test.html')   


def index(request):
	return render(request,'indexoffaculty.html')

def doLogin(request):
    if request.method == "POST":
       user = EmailBackEnd.authenticate(request,
                                        username=request.POST.get('email'),
                                        password=request.POST.get('password'),)
       print("hello",user)
       if user!=None:
           login(request,user)
           user_type = user.user_type
           if user_type == '1':
               return redirect('hodhome')
           elif user_type == '2':
               #return HttpResponse('This is Staff Panel')
                return redirect('staffhome')

           elif user_type == '3':
                return redirect('studenthome')
           else:
               messages.error(request,'Email and Password Are Invalid !')
               return redirect('login')
       else:
           messages.error(request,'Email and Password Are Invalid !')
           return redirect('login')
def dologout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/')
def PROFILE(request):
    user = CustomUser.objects.get(id = request.user.id)


    context = {
        "user":user,
    }
    return render(request,'Hod/profiles.html',context)
@login_required(login_url='/')
def PROFILE_UPDATE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        #email = request.POST.get('email')
        #username = request.POST.get('username')
        password = request.POST.get('password')
        print(profile_pic)
        try:
            customuser = CustomUser.objects.get(id = request.user.id)

            customuser.first_name = first_name
            customuser.last_name = last_name

            if password !=None and password != "":
                customuser.set_password(password)
            if profile_pic !=None and profile_pic != "":
                customuser.profile_pic = profile_pic
            customuser.save()
            messages.success(request,'Your Profile Updated Successfully !')
            return redirect('profile')
        except:
            messages.error(request,'Failed To Update Your Profile')

    return render(request,'Hod/profiles.html')

