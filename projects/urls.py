#projects/urls.py

from django.urls import path
from projects import views

urlpatterns = [
    path("", views.project_index, name="project_index"),#connect the rool URL of the project app to the
    # project_index view
    path("<int:pk>/", views.project_detail, name="project_detail"),
    # It is slightly more complicated to connect the project_detail view. You want the URL to be /1,/2
    # or whatever number corresponds to the primary key of the project. The pk value in the URL is the 
    # same pk passes to the view function, so you need to dynamically generate these URLs depending on which
    # project you what to view. To do this, you use the <int:pk> notation.
    # This notation tells Django that the value pased inthe URL is an integar, and its variable name is pk.
    # That's the parameter of your project_detail(view) function.
]