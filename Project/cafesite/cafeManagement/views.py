from django.shortcuts import render,redirect
from .forms import AccountForm
from .models import Account
import requests
import json

global token

def acIndex(request):
    return render(request,"cafeManagement/base.html")

def acLogout(request):
    del request.session["access_token"]
    del request.session["username"]
    #need to add token to blocklist
    return render(request,"cafeManagement/login.html")

def acLogin(request):
    if request.method=="POST":
        print(type(request), request)
        user=request.POST["username"]
        pasword=request.POST["password"]
        send_data=dict(acno=user, password=pasword)
        print(type(send_data), send_data)
        response=requests.post("http://127.0.0.1:5000/login", json=send_data).json()
        print(type(response), response)
        if "access_token" in response:
            request.session["access_token"]=response["access_token"]
            request.session["username"]=response["username"]
            return render(request,"cafeManagement/home.html", context={"response":response,"session":request.session["user"]})
        else:
            return render(request,"cafeManagement/login.html")
    else:
        return render(request,"cafeManagement/login.html")
   

def acForm(request):
    if request.method=="POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            name=request.POST["name"]
            dob=request.POST["dob"]
            aadhar=request.POST["aadhar"]
            mobile=request.POST["mobile"]
            email=request.POST["email"]
            password=request.POST["password"]
            actype=request.POST["actype"]
            send_data=dict(name=name,dob=dob,aadhar=aadhar,mobile=mobile,email=email,password=password,actype_id=actype)
            print(type(send_data), send_data)
            response=requests.post("http://127.0.0.1:5000/account", json=send_data).json()
            print(type(response), response)
            return render(request,"cafeManagement/list.html",{"response":response})
    else:
        form = AccountForm() 
        return render(request,"cafeManagement/form.html",{"form":form})

def acView(request):
    return render(request,"cafeManagement/view.html")

def acUpdate(request):
    return render(request,"cafeManagement/update.html")

def acDelete(request):
    return render(request,"cafeManagement/delete.html")

def acList(request):
    response=requests.get("http://127.0.0.1:5000/user").json()
    return render(request,"cafeManagement/list.html",{"response":response})


def achome(request):
    token=request.session["user"]
    return render(request,"cafeManagement/home.html")