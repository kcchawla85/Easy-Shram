from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from .models import AdminUser, UserLabour, PostedJobs
from datetime import datetime, timedelta
from django.utils import timezone


# Create your views here.

def home(request):
    return render(request, 'home.html')

def ulogin(request):
    if(request.method=="POST"):
        username = request.POST['Username']
        password = request.POST['Pswd']

        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/user-job-form")

    return render(request, 'user-login.html')

def createuser(request):
    if(request.method=="POST"):
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['username']
        password = request.POST['Pswd']
        cpassword = request.POST['CPswd']
        shramcard = request.POST['shramcard']
        aadhar = request.POST['Aadharcard']
        contact = request.POST['PhoneNumber']

        if(User.objects.filter(username=username).exists()):
            return render(request, 'user-login.html', {'usersignuperror':"Username already taken."})

        else:
            if(password==cpassword):
                user=User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password)
                user.save()

                user=auth.authenticate(username=username, password=password)
                if user is not None:
                    auth.login(request, user)
                    UserLabour.objects.create(user=user, shramcard=shramcard, aadhar=aadhar, contact=contact)
                    return redirect("/user-job-form")
            
            else:
                return render(request, 'user-login.html', {'usersignuperror':"The password you entered did not matched."})

def alogin(request):
    if(request.method=="POST"):
        username = request.POST['Username']
        password = request.POST['pswd']

        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/post-a-job")
        
    return render(request, 'admin-login.html')

def createadmin(request):
    if(request.method=="POST"):
        username = request.POST['Username']
        password = request.POST['pswd']
        cpassword = request.POST['cpswd']
        aadhar = request.POST['Aadhar-card']
        contact = request.POST['Mobile-Number']

        if(User.objects.filter(username=username).exists()):
            return render(request, 'admin-login.html', {'adminsignuperror':"Username already taken."})

        else:
            if(password==cpassword):
                user=User.objects.create_user(username=username, password=password)
                user.save()

                user=auth.authenticate(username=username, password=password)
                if user is not None:
                    auth.login(request, user)
                    AdminUser.objects.create(user=user, aadhar=aadhar, contact=contact)
                    return redirect("/post-a-job")
            
            else:
                return render(request, 'admin-login.html', {'adminsignuperror':"The password you entered did not matched."})

def userjobform(request):
    if(request.method=="POST"):
        category = request.POST['category']
        pincode = request.POST['pincode']
        output = PostedJobs.objects.filter(category=category).filter(pincode=pincode)
        return render(request, 'result.html', {"output":output})
    return render(request, 'user-form.html')

def postjob(request):
    if(request.method=="POST"):
        category = request.POST['category']
        title = request.POST['Jobtitle']
        pay = request.POST['payscale']
        age = request.POST['Age']
        contact = request.POST['contact']
        state = request.POST['state']
        pincode = request.POST['pincode']

        PostedJobs.objects.create(category=category, jobtitle=title, pay=pay, age=age, contact=contact, state=state, pincode=pincode)

        return render(request, 'post-a-job.html', {"jobposted":"true"})
    return render(request, 'post-a-job.html')