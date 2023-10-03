#projects/views.py

from django.shortcuts import render
from projects.models import Project #function from the projects/models.py

def project_index(request):
    projects = Project.objects.all()# perform a query. A query is a command that allows you to create, retrieve
    #update, or delete objects(or rows) in your database. In this case, you're retrieving all the objects in the
    #projects table.
    context= {
        "projects" : projects # you define a dictionary named context. The dictionary only has one entry--projects,
    }                        # to which you assign your Queryset containing all the projects.
                             # Django uses the context dictionary to send information to your template.
    return render(request, "projects/project_index.html",context) 
    # you add context as an argument to render(). Any entries in the context dictionary are available
    # in the template, as long as you pass the context argument to render(). You will need to create
    # a context dictionary and pass it to render in each view function that you create.
    # you also add the path to a template named project_index.html to render()

def project_detail(request, pk):
    project = Project.objects.get(pk=pk) # another query, this query retrieves the project with a primary key,
                                         # pk, equal to the function's argument. This primary key is unique
                                         # identifier of a database entry. 
    context = {
        "project":project
    }
    return render(request, "projects/project_detail.html",context)
"""
A database query returns a collection of all the objects that match the query, 
known as a Queryset. In this case, you want all the objects in the table, 
so it will return a collection of the three projects that you created before.
"""
