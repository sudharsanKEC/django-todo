from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import CTO
# Create your views here.
def ctoAuthSignup(request):
    if request.method=="POST":
        name=request.POST['name']
        company=request.POST['company']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1!=password2:
            return render(request,'cto_signup.html',{"error":"The password entered should match each other"})

        if CTO.objects.filter(name=name,company_name=company).exists():
            return render(request,'cto_signup.html',{"error":"CTO already exists"})
        else:
            cto = CTO.objects.create(name=name,company_name=company,password=password1)
            return redirect("ctoAuthLogin")
    return render(request,"cto_signup.html")
def ctoAuthLogin(request):
    if request.method=="POST":
        name=request.POST["name"]
        company=request.POST["company"]
        password=request.POST["password"]
        cto = CTO.objects.filter(name=name,company_name=company).first()

        if cto:
            if cto.password==password:
                request.session["cto_id"]=cto.cto_id
                return redirect("ctopage")
            else:
                messages.error(request,"Invalid credentials! Please verify your inputs")
                return redirect("ctoAuthLogin")
        else:
            messages.error(request,"Invalid credentials! Please verify your inputs")
            return redirect("ctoAuthLogin")
    return render(request,"cto_login.html")

def ctopage(request):
    cto_id=request.session.get("cto_id",0)
    if not cto_id:
        return redirect('ctoauthlogin')
    cto=CTO.objects.get(cto_id=cto_id)
    return render(request,"cto_dashboard.html",{"cto":cto})