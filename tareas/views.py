from django.shortcuts import render
from django.http import HttpResponse
from models import Evento
# Create your views here.

def reporte_estado(request):
    lista_resumen=[]

    lista_eventos=Evento.objects.all()

    for evento in lista_eventos:
        resumen = {}
        resumen['evento']= evento
        resumen['tareas_cantidad']=evento.tarea_set.count()
        resumen['tareas_completas']=evento.tarea_set.filter(completado=True).count()
        try:
            resumen['porcentaje_completado']=int(float(resumen['tareas_completas'])/resumen['tareas_cantidad']*100)
        except:
            resumen['porcentaje_completado']=0

        lista_resumen.append(resumen)

    return render(request,'reporte_estado.html',{'lista_resumen':lista_resumen})


def sobre(request):
    return HttpResponse('OK')

