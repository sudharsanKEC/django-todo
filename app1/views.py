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
        elif role=="SPM":
            return redirect("spmAuthLogin")
        else:
            return redirect("emp_login",role=role)
        

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
    return render(request,"cto/cto_signup.html")
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
    emps=EMP_Role.objects.filter(emp_spm=id)
    return render(request,'SPM/dashboard.html',
                    {
                      "spm":spm,
                      "tasks":tasks,
                      "emps":emps,
                    }
                  )


# def spm_role_creation(request,spm_id):
#     spm=SPM.objects.filter(spm_id=spm_id).first()
#     tasks=SPM_TASK.objects.filter(assigned_to=spm_id).first()
#     if request.method=="POST":
#         name=request.POST.get('name')
#         role=request.POST.get('role')
#         password1=request.POST.get('password')
#         password2=request.POST.get('confirm-password')
#         if password1!=password2:
#             messages.error(request,"Passworda does not matches correctly for the previous role creation!")
#             return redirect('spm_dashboard',name=spm.name,id=spm.spm_id) # the names(name,id) given here should have the same name in the url also, i mean the names here and there should be similar if not then it will cause error
#         if role=="senior-dev":
#             Senior_dev.objects.create(sde_spm=spm,sde_cto=spm.cto,name=name,password=password1) # here we should not give like this Senior_dev.objects.create(sde_spm=spm.spm_id,sde_cto=spm.cto.cto_id,name=name,password=password1) because when we try to assign the value for a foreign key field in a model, we should not want to give like sde_spm=spm.spm_id and sde_cto=spm.cto.cto_id because django automatically takes the primary key from the model when we give like sde_spm=spm so we dont want to assign like sed_spm=spm.spm_id if we do so then it might leads to some unexpected behavior
#             messages.success(request,f"User {name} with {role} role created successfully")
#             return redirect('spm_dashboard',name=spm.name,id=spm.spm_id)
#     return render(request,"SPM/dashboard.html",{"spm":spm,"tasks":tasks})


def toggle_spm_task_checkbox(request,task_id):
    if request.method=="POST":
        task=get_object_or_404(SPM_TASK,id=task_id)
        if request.POST.get("task_status")=="on":
            task.status="Completed"
        else:
            task.status="Pending"
        task.save()
        return redirect("spm_dashboard",name=task.assigned_to.name,id=task.assigned_to.spm_id)

def spm_role_creation(request,spm_id):
    spm_obj=SPM.objects.get(spm_id=spm_id)
    
    if not spm_obj:
        return redirect('spmAuthLogin')
    cto_obj=spm_obj.cto
    if request.method=="POST":
        name=request.POST.get('name')
        role=request.POST.get('role')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1==password2:
            EMP_Role.objects.create(role=role,name=name,password=password1,emp_cto=cto_obj,emp_spm=spm_obj,company=cto_obj.company_name)
            messages.success(request,f"employee {name} created with the role {role} successfully")
            return redirect("spm_dashboard",name=spm_obj.name,id=spm_obj.spm_id)
        else:
            messages.error(request,"Both the entered password should match")
    emps=EMP_Role.objects.filter(emp_spm=spm_obj)

    
    return render(request,"SPM/dashboard.html",
                  {
                      "emps":emps,
                      "spm":spm_obj,
                  }
                )
    

def spm_assign_task_emp(request,emp_id):
    emp_obj=EMP_Role.objects.filter(emp_id=emp_id).first()
    tasks=EMP_task1.objects.filter(assigned_to=emp_obj)
    return render(request,"SPM/spm_assign_task_emp.html",
                  {
                      "emp":emp_obj,
                      "tasks":tasks,
                  }
                  )

def emp_task_creation(request,emp_id):
    emp_obj=EMP_Role.objects.filter(emp_id=emp_id).first()
    spm_id=emp_obj.emp_spm.spm_id
    spm_obj=SPM.objects.filter(spm_id=spm_id).first()
    
    if request.method=="POST":
        title=request.POST.get('title')
        description=request.POST.get('task_description')
        
        EMP_task1.objects.create(
            title=title,
            description=description,
            assigned_to=emp_obj,
            created_by=spm_obj
        )
        messages.success(request,"Task assigned successfully")
        return redirect("spm_assign_task_emp",emp_obj.emp_id)
    tasks=EMP_task1.objects.filter(assigned_to=emp_id)
    return render(request,"SPM/spm_assign_task_emp.html",
                  {
                    "tasks":tasks,    
                  }
                  )

# def emp_to_login(request):
#     if request.method=="POST":
#         emp_role=request.POST.get("role")
#         return render(request,"employee/login.html",{"emp_role":emp_role})
#     return render(request,"home.html")

def emp_login(request,role): 
    if request.method=="POST":
        company=request.POST.get("company")
        name=request.POST.get("name")
        password=request.POST.get("password")


        emp_comp=CTO.objects.filter(company_name=company).first()
        if not emp_comp:
            messages.error(request,"No company exists with that name")
            return redirect("emp_login",role=role)     

        emp_obj=EMP_Role.objects.filter(company=company,name=name,role=role).first()
        
        if emp_obj:
            if emp_obj.password==password:
                return redirect("emp_home",name=name,role=role,company=company)
            else:
                messages.error(request,"Incorrect password!")
                return redirect("emp_login",role=role)
        messages.error(request,"No user exists with that role")
        return redirect("emp_login",role=role)
       
    return render(request,"employee/login.html",{"role":role})    

def emp_home(request,name,role,company):
    emp_obj=EMP_Role.objects.filter(name=name,role=role,company=company).first()
    emp_task_obj=EMP_task1.objects.filter(assigned_to=emp_obj)
    return render(request,"employee/home.html",{"name":name,"role":role,"company":company,"emp_tasks":emp_task_obj}) 
 
def toggle_emp_task_checkbox(request,task_id):
    if request.method=="POST":
        task_obj=EMP_task1.objects.filter(id=task_id).first()
        if request.POST.get("task_status")=="on":
            task_obj.status="Completed"
        else:
            task_obj.status="Pending"
        task_obj.save()
        return redirect("emp_home",name=task_obj.assigned_to.name,role=task_obj.assigned_to.role,company=task_obj.assigned_to.company)

def emp_delete_task(request,id):
    task_obj=EMP_task1.objects.filter(id=id).first()
    emp_id=task_obj.assigned_to.emp_id
    if request.method=="POST":
        task_obj.delete()
        messages.success(request,"Task deleted successfully")
        return redirect("spm_assign_task_emp",emp_id=emp_id)