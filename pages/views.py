#pages/views.py
from django.shortcuts import render
from pages.models import profile
from pages.models import aboutme
from projects.models import Project

# Create your views here.
def home(request):
    myprofile = profile.objects.first()
    picdescription = myprofile.description
    profilepic = myprofile.image
    aboutmetext = aboutme.objects.first()
    projects = Project.objects.all()
    context = {
        'pic' : profilepic,
        'discription' : picdescription,
        'text' : aboutmetext,
        "projects" : projects
    }
    return render(request, "pages/home.html", context)