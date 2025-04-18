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

class SPM_TASK(models.Model):
    title=models.CharField(max_length=255,blank=False,null=False)
    description=models.TextField()
    assigned_to=models.ForeignKey(SPM,on_delete=models.CASCADE,related_name="tasks")
    created_by=models.ForeignKey(CTO,on_delete=models.CASCADE,related_name="assigned_tasks")
    status=models.CharField(max_length=20,choices=[("Pending","Pending"),("Completed","Completed")],default="Pending")
    created_at=models.DateTimeField(auto_now_add=True)
    
class Senior_dev(models.Model):
    sde_id=models.AutoField(primary_key=True)
    sde_spm=models.ForeignKey(SPM,on_delete=models.CASCADE,related_name="sde_spm")
    sde_cto=models.ForeignKey(CTO,on_delete=models.CASCADE,related_name="sde_cto")
    name=models.CharField(max_length=100,blank=False,null=False)
    password=models.CharField(max_length=100,blank=False,null=False)

class UIUX(models.Model):
    uiux_id=models.AutoField(primary_key=True)
    uiux_spm=models.ForeignKey(SPM,on_delete=models.CASCADE,related_name="uiux_spm")
    uiux_cto=models.ForeignKey(CTO,on_delete=models.CASCADE,related_name="uiux_cto")
    name=models.CharField(max_length=100,blank=False,null=False)
    password=models.CharField(max_length=100,blank=False,null=True)

class DEVOPS(models.Model):
    dops_id=models.AutoField(primary_key=True)
    dops_spm=models.ForeignKey(SPM,on_delete=models.CASCADE,related_name="dops_spm")
    dops_cto=models.ForeignKey(CTO,on_delete=models.CASCADE,related_name="dops_cto")
    name=models.CharField(max_length=100,blank=False,null=False)
    password=models.CharField(max_length=100,blank=False,null=False)

class NE(models.Model):
    ne_id=models.AutoField(primary_key=True)
    ne_spm=models.ForeignKey(SPM,on_delete=models.CASCADE,related_name="ne_spm")
    ne_cto=models.ForeignKey(CTO,on_delete=models.CASCADE,related_name="ne_cto")
    name=models.CharField(max_length=100,blank=False,null=False)
    password=models.CharField(max_length=100,blank=False,null=False)

class Intern(models.Model):
    intern_id=models.AutoField(primary_key=True)
    intern_spm=models.ForeignKey(SPM,on_delete=models.CASCADE,related_name="intern_spm")
    intern_cto=models.ForeignKey(CTO,on_delete=models.CASCADE,related_name="intern_cto")
    name=models.CharField(max_length=100,blank=False,null=False)
    password=models.CharField(max_length=100,blank=False,null=False)