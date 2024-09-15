from django.contrib import admin
from cms.models import Case, Service, Methodology, Note, Ressource, Privesc

class CaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'webpage', 'address', 'description', 'state', 'OS', 'last_update', 'type_of_target')

class MethodologyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'related_port')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'port', 'version', 'checked', 'vulnerable', 'linked_methodology', 'linked_case')

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'date', 'linked_case')

class RessourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'linked_methodology')

class PrivescAdmin(admin.ModelAdmin):
    list_display = ('os', 'text')

admin.site.register(Case, CaseAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Methodology, MethodologyAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Ressource, RessourceAdmin)
admin.site.register(Privesc, PrivescAdmin)