from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import *
# Create your views here.

def home(request):
    return render(request,"home.html")
def login_redirect(request):
    if request.method=="POST":
        role=request.POST.get('role')

        if role=="CTO":
            return redirect("ctoAuthLogin")
        if role=="SPM":
            return redirect("spmAuthLogin")
        if role=="PM":
            return redirect("pmAuthLogin")
        if role=="SD":
            return redirect("seniordevAuthLogin")
        if role=="Intern":
            return redirect("internAuthLogin")
        if role=="uiux":
            return redirect("uiuxAuthLogin")
        if role=="devops":
            return redirect("devopsAuthLogin")
        if role=="network":
            return redirect("networkAuthLogin")

def ctoAuthSignup(request):
    if request.method=="POST":
        name=request.POST['name']
        company=request.POST['company']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1!=password2:
            return render(request,'cto/cto_signup.html',{"error":"The password entered should match each other"})

        if CTO.objects.filter(name=name,company_name=company).exists():
            return render(request,'cto/cto_signup.html',{"error":"CTO already exists"})
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
    return render(request,"cto/cto_login.html")

def ctopage(request):
    cto_id=request.session.get("cto_id",0)
    if not cto_id:
        return redirect('ctoauthlogin')
    
    cto=CTO.objects.get(cto_id=cto_id)

    if request.method=="POST":
        name=request.POST["name"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        if password1==password2:
            SPM.objects.create(name=name,password=password1,cto=cto)
            messages.success(request,f"Senior product manager {name} created successfully")
            return redirect('ctopage')
        else:
            messages.error(request,"Enter the inputs properly!")
    
    spms = SPM.objects.filter(cto=cto)

    return render(request,"cto/cto_dashboard.html",
                    {
                        "cto":cto,
                        "spms":spms,
                    }
                )






def cto_spm(request,spm_id):
    spm=get_object_or_404(SPM,spm_id=spm_id)
    if request.method=="POST":
        title=request.POST["title"]
        description=request.POST["description"]
        cto=CTO.objects.get(cto_id=request.session["cto_id"])

        SPM_TASK.objects.create(
            title=title,
            description=description,
            assigned_to=spm,
            created_by=cto
        )
        messages.success(request,"Task Assigned successfully")
        return redirect("cto_spm",spm_id=spm.spm_id)
    tasks=SPM_TASK.objects.filter(assigned_to=spm)
    return render(request,"cto/cto_assign_task.html",{"spm":spm,"tasks":tasks})

def delete_task(request,t_id):
    task=get_object_or_404(SPM_TASK,id=t_id)
    spm_id=task.assigned_to.spm_id

    if request.method=="POST":
        task.delete()
        messages.success(request,"Task deleted successfully")
    return redirect("cto_spm",spm_id=spm_id)



def spmAuthLogin(request):

    if request.method=="POST":
        name=request.POST.get("name")
        password=request.POST.get("password")
        company=request.POST.get("company")

        print("Entered details: ",name,password,company)

        cto = CTO.objects.filter(company_name=company).first()

        if not cto:
            messages.error(request,f"No company exists with this {company} name")
            return redirect('spmAuthLogin')
        spm = SPM.objects.filter(name=name,password=password,cto_id=cto.cto_id).first()        
        if spm:
           return redirect('spm_dashboard',name=spm.name,id=spm.spm_id)
        else:
            messages.error(request,"Invalid credentials!")
            return redirect('spmAuthLogin')
        
    return render(request,"SPM/login.html")

def spm_dashboard(request,name,id):
    spm=SPM.objects.filter(spm_id=id).first()
    tasks=SPM_TASK.objects.filter(assigned_to=spm.spm_id)
    return render(request,'SPM/dashboard.html',{"spm":spm,"tasks":tasks})

def toggle_spm_task_checkbox(request,task_id):
    if request.method=="POST":
        task=get_object_or_404(SPM_TASK,id=task_id)
        if request.POST.get("task_status")=="on":
            task.status="Completed"
        else:
            task.status="Pending"
        task.save()
        return redirect("spm_dashboard",name=task.assigned_to.name,id=task.assigned_to.spm_id)

def pmAuthLogin(request):
    return HttpResponse("<h1>Product Manager login page</h1>")

def internAuthLogin(request):
    return HttpResponse("<h1>Intern Login page</h1>")

def uiuxAuthLogin(request):
    return HttpResponse("<h1>UIUX login page</h1>")

def devopsAuthLogin(request):
    return HttpResponse("<h1>Devops Login page</h1>")

def networkAuthLogin(request):
    return HttpResponse("<h1>Network login page</h1>")

def seniordevAuthLogin(request):
    return HttpResponse("<h1>Senior developer login page</h1>")
