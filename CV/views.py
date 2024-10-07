from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from CV.models import competance,stage,formation

def index(request):
    template=loader.get_template('infosGenerales.html')
    context={
        'mail':'youssefhammemy56@gmail.com',
        'telephone':'52807531',
        'adresse': 'Tunis,Zaghouen '  ,
        'datedenaissance':'05 february 2003'  
    }
    return HttpResponse(template.render(context,request))
def list_comp(request):    
    comp=competance.objects.all().values
    template=loader.get_template('competances.html')
    context={
        'comp':comp,
    }
    return HttpResponse(template.render(context,request))
def list_stage(request):
    stg=stage.objects.all().values
    template=loader.get_template('stage.html')
    context={
        'stg':stg,
    }    
    return HttpResponse(template.render(context,request))
def list_formation(request):
    form=formation.objects.all().values
    template=loader.get_template('formation.html')
    context={
        'form':form
    }

    return HttpResponse(template.render(context,request))
    



   


