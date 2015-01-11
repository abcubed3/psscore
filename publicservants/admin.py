from django.contrib import admin

# Register your models here.
from .models import PublicServant


class PublicServantAdmin(admin.ModelAdmin):
    class Meta:
        model= PublicServant
        

admin.site.register(PublicServant, PublicServantAdmin)
    
