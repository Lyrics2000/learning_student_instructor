from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate,login
from .models import UserTable
from .form import (
    SignINForm,
    SignUpForm
)



def logout_user(request):
    if request.method=="POST":
        logout(request)
        return HTTPResponse("lOGGED OUT SUCCESSFULLY")


def signIn(request):
    login_form = SignINForm(request.POST,None)

    
    context = {
        'login' : login_form
    }

    if login_form.is_valid:
        username = request.POST.get("username")
        password = request.POST.get("password")
        print("username and password ",username,password)
        user = authenticate(request,username = username, password = password )
        print("jjja",user)
        if user is not None:
            # login(request,user)
            print("hhs",user.id)
            obj = UserTable.objects.get(id = user.id)
            if(obj.userType == "STUDENT"):
                login(request,user)
                return redirect("student:studentDashboard")

            else:
                login(request,user)
                request.session['topic']  =  None
                return redirect("instructor:instructor")

        else:
            pass


    return render(request,'signIn.html',context)


def signUp(request):
    return render(request,'signUp.html')
