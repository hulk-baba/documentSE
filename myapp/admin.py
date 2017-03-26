from django.contrib import admin
from .models import Documents

# Register your models here.

class DocAdmin(admin.ModelAdmin):
	pass
	
admin.site.register(Documents, DocAdmin)