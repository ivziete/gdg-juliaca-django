from django.contrib import admin
from models import Tarea,Evento

# Register your models here.
class TareaAdmin(admin.ModelAdmin):
    list_display=['titulo','completado','fecha_creacion','prioridad','evento']
    search_fields=['titulo']

class TareaInline(admin.TabularInline):
    model=Tarea

class EventoAdmin(admin.ModelAdmin):
    list_diplay=['titulo']
    inlines = [TareaInline]

admin.site.register(Evento,EventoAdmin)
admin.site.register(Tarea,TareaAdmin)