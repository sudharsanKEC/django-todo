from django.contrib import admin
from .models import *
# Register your models here.
class CTOAdmin(admin.ModelAdmin):
    list_display=['cto_id','name','company_name','password']
    ordering=['cto_id']
admin.site.register(CTO,CTOAdmin)