from django.shortcuts import render
from .forms import RegistrationForm,LoginForm
from .models import RegistrationData
from django.http.response import HttpResponse

def registration_view(request):
    if request.method=="POST":
        rform=RegistrationForm(request.POST)
        if rform.is_valid():
            fname=request.POST.get("firstname")
            lname=request.POST.get('lastname')
            uname=request.POST.get('username')
            pwd=request.POST.get('password')
            mobile=request.POST.get('mobile')
            email=request.POST.get('email')
            gender=rform.cleaned_data.get('gender')
            dob=rform.cleaned_data.get('date_of_birth')

            data=RegistrationData(
                firstname=fname,
                lastname=lname,
                username=uname,
                password=pwd,
                mobile=mobile,
                email=email,
                gender=gender,
                date_of_birth=dob
            )
            data.save()
            rform=RegistrationForm()
            return render(request,'reg.html',{'rform':rform})
        else:
            return HttpResponse("user missed some data")
    else:
        rform=RegistrationForm()
        return render(request,'reg.html',{'rform':rform})

def login_view(request):
    if request.method=="POST":
        lform=LoginForm(request.POST)
        if lform.is_valid():
            uname=request.POST.get('username')
            pwd=request.POST.get('password')

            uname1=RegistrationData.objects.filter(username=uname)
            pwd1=RegistrationData.objects.filter(password=pwd)

            if uname and pwd:
                return HttpResponse("success")
            else:
                return HttpResponse("failed")
        else:return HttpResponse("user missed data")
    else:
        lform=LoginForm()
        return render(request,'log.html',{'lform':lform})








