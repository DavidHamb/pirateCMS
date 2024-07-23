from django.contrib import admin
from cms.models import Case, Service, Methodology

class CaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'webpage', 'address', 'description', 'state', 'OS', 'last_update')

class MethodologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'cve', 'related_service', 'version', 'documents', 'urls')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'port', 'version', 'checked', 'vulnerable', 'address', 'methodology')

admin.site.register(Case, CaseAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Methodology, MethodologyAdmin)
