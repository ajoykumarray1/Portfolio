from django.shortcuts import render
from .models import *

# Create your views here.
def Home(request):
    about=About.objects.first()
    services=Service.objects.all()
    works=RecentWork.objects.all()
    context={
        'about':about,
        'services':services,
        'works':works
    }
    return render(request,'home.html',context)