from django.contrib import admin
from .models import Red

# Register your models here.
class RedAdmin(admin.ModelAdmin):
    pass

admin.site.register(Red, RedAdmin)