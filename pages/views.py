#pages/views.py
from django.shortcuts import render
from pages.models import profile
from pages.models import aboutme

# Create your views here.
def home(request):
    myprofile = profile.objects.first()
    picdescription = myprofile.description
    profilepic = myprofile.image
    aboutmetext = aboutme.objects.first()
    context = {
        'pic' : profilepic,
        'discription' : picdescription,
        'text' : aboutmetext
    }
    return render(request, "pages/home.html", context)