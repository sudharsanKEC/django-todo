from django.db import models

# Create your models here.
class CTO(models.Model):
    cto_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,null=False,blank=False)
    company_name=models.CharField(max_length=100,null=False,blank=False)
    password=models.CharField(max_length=100,null=False,blank=True)
    