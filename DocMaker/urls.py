from django.conf.urls import handler404
from django.urls import path

from . import views





urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("subjectselection",views.subjectselection,name="subjectselection"),
    path("template",views.templateCreation,name="templateCreation"),
    path('addsubject',views.AddSubject,name="addSubject"),
    path('addExperiment',views.AddExperiment,name="addExperiment"),
    path('edit/<int:id>/',views.editExperiment,name="editExperiment")



]



