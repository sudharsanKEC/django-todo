from django.db import models

# Create your models here.
class CTO(models.Model):
    cto_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,null=False,blank=False)
    company_name=models.CharField(max_length=100,null=False,blank=False)
    password=models.CharField(max_length=100,null=False,blank=True)
    
    def __str__(self):
        return self.name

class SPM(models.Model):
    spm_id=models.AutoField(primary_key=True)
    cto=models.ForeignKey(CTO,on_delete=models.CASCADE,related_name='spms')
    name=models.CharField(max_length=100,blank=False,null=False)
    password=models.CharField(max_length=100,blank=False,null=False)
    def __str__(self):
        return self.name

class SPM_TASK(models.Model):
    title=models.CharField(max_length=255,blank=False,null=False)
    description=models.TextField()
    assigned_to=models.ForeignKey(SPM,on_delete=models.CASCADE,related_name="tasks")
    created_by=models.ForeignKey(CTO,on_delete=models.CASCADE,related_name="assigned_tasks")
    status=models.CharField(max_length=20,choices=[("Pending","Pending"),("Completed","Completed")],default="Pending")
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:  
        verbose_name_plural="SPM Tasks"   
    def __str__(self):
        return self.title
    
class EMP_Role(models.Model):
    emp_id=models.AutoField(primary_key=True)
    role=models.CharField(max_length=25,blank=False,null=False)
    emp_spm=models.ForeignKey(SPM,on_delete=models.CASCADE,related_name="emp_spm")
    emp_cto=models.ForeignKey(CTO,on_delete=models.CASCADE,related_name="emp_cto")
    name=models.CharField(max_length=100,blank=False,null=False)
    password=models.CharField(max_length=100,blank=False,null=False)
    company=models.CharField(max_length=25,blank=False,null=False)
    class Meta:
        verbose_name_plural="Employees"
    def __str__(self):
        return f"{self.name},{self.role},{self.company}"

class EMP_task1(models.Model):
    title=models.CharField(max_length=100,blank=False,null=False)
    description=models.TextField()
    assigned_to=models.ForeignKey(EMP_Role,on_delete=models.CASCADE,related_name="emp")
    created_by=models.ForeignKey(SPM,on_delete=models.CASCADE,related_name="spm_emp")
    status=models.CharField(max_length=20,choices=[("Pending","Pending"),("Completed","Completed")],default="Pending")
    created_at=models.DateTimeField(auto_now_add=True)  
    class Meta:
        verbose_name_plural="Employee tasks"