from django.contrib import admin
from .models import *
# Register your models here.
class CTOAdmin(admin.ModelAdmin):
    list_display=['cto_id','name','company_name']
    ordering=['cto_id']
admin.site.register(CTO,CTOAdmin)

class SPMAdmin(admin.ModelAdmin):
    # readonly_fields=['cto',]
    list_display=['spm_id','name','password','get_cto_name','get_cto_id']
    ordering=['spm_id']
    @admin.display(description='CTO Name') # how its correctly displaying the name in admin panel?
    def get_cto_name(self,obj):
        return obj.cto.name
    @admin.display(description='CTO Id')
    def get_cto_id(self,obj):
        return obj.cto.cto_id
admin.site.register(SPM,SPMAdmin)