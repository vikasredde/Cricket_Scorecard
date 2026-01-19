from django.shortcuts import render
from . import models

def home(request):
    teams=models.Team.objects.all()

    # render(request, template_name, context)
    return render(request,'cricket/home.html',{'teams':teams})
