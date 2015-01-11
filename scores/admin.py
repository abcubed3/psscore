from django.contrib import admin

from .models import Score


# Register your models here.
class ScoreAdmin(admin.ModelAdmin):
    class Meta:
        model= Score
        

admin.site.register(Score, ScoreAdmin)
    
