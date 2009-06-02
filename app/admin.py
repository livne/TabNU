from django.contrib import admin
from models import Tab

class TabAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'remark', 'active', 'updated',]
    list_filter = ['active',]
    search_fields = ['name', 'title', 'remark', 'url',]

admin.site.register(Tab, TabAdmin)
