from django.shortcuts import render,redirect
from .forms import AccountForm
from .models import Account
import requests
import json

def acIndex(request):
    return render(request,"cafeManagement/base.html")

def acLogout(request):
    if 'access_token' in request.session:
        auth="Bearer "+str(request.session["access_token"])
        print(type(auth), auth)
        response=requests.post("http://127.0.0.1:5000/logout",headers={"Authorization":auth}).json()
        print("Response from logout",type(response), response)
        if "msg" in response:
            if response["msg"]=="Signature verification failed":
                print("Invalid Signature !!!!!!!")
                return redirect("../login")
            elif response["msg"]=="Missing Authorization Header":
                print('Authorization missing!')
                response["access_token"]=request.session["access_token"]
                response["acno"]=request.session["acno"]
                return render(request,"cafeManagement/home.html", context={"response":response})
            elif response["msg"]=="Token has expired":
                print('Token expired!')
                return redirect("../login")
            elif response["msg"]=="Logged-out Successfully":
                del request.session["access_token"]
                del request.session["acno"]
                print('Logged-out Successfully & session deleted!')
                return redirect("../login")
            else:
                return print("Problem Problem 222 !!!!!!")
        else:
            return print("Problem Problem 333 !!!!!!")
    else:
        print('access_token missing login first!')
        return redirect("../login")
    
    

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
            request.session["acno"]=response["acno"]
            return render(request,"cafeManagement/home.html", context={"response":response})
        else:
            return redirect("../login")
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

def acHome(request):
    return render(request,"cafeManagement/home.html")

def acCredit(request):
    return render(request,"cafeManagement/credit.html")

def acDebit(request):
    return render(request,"cafeManagement/debit.html")