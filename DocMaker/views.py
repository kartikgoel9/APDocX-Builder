from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import User, UserCurrentSelectedSubjects, Experiments, Subject
from .forms import *

from docx.enum.text import WD_ALIGN_PARAGRAPH

from docx.enum.text import WD_ALIGN_PARAGRAPH
from docxtpl import DocxTemplate, InlineImage, R

from docx.shared import Inches, Mm
from docx.shared import Pt

from django.contrib.auth.decorators import login_required



from django.utils.encoding import smart_str
from django.templatetags.static import static

from wsgiref.util import FileWrapper

import os


import time






   


def index(request):
    experiments = Experiments.objects.all()
    experimentList = list()
    for experiment in experiments:
        if str(experiment.experiment_owner) == str(request.user):
            experimentList.append(experiment)

    context = {'experiments': experimentList}

    return render(request, "DockMaker/index.html", context)

@login_required
def editExperiment(request, id):
    experiment = Experiments.objects.get(pk=id)
    subjectName = experiment.experiment_name
    if request.method != 'POST':
        form = editExperimentForm({'aim': experiment.aim, 'source_code': experiment.source_code})

    else:
        experiment.aim = request.POST.get('aim')
        experiment.source_code = request.POST.get('source_code')
        experiment.save()
        return redirect('index')
    context = {'form': form, 'id': id, 'subject': subjectName}
    return render(request, "DockMaker/editExperiment.html", context)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "Dockmaker/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "DockMaker/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "DockMaker/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "DockMaker/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "DockMaker/register.html")

@login_required
def AddSubject(request):
    if request.method != 'POST':
        form = addSubject()
    else:
        form = addSubject(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.subject_owner = request.user
            new_form.save()
            return redirect('addExperiment')
    context = {'form': form}
    return render(request, "DockMaker/addSubject.html", context)

@login_required
def AddExperiment(request):
    subjects = Subject.objects.all()
    lst = []
    for subject in subjects:
        if str(subject.subject_owner) == str(request.user):
            print(subject.id)
            lst.append(subject)
    if request.method != 'POST':
        form = addExperiment()
    else:
        form = addExperiment(request.POST,request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.experiment_owner = request.user
            new_form.save()
            return redirect('index')
    context = {'form': form, 'subjects': lst}
    return render(request, "DockMaker/addExperiment.html", context)

@login_required
def subjectselection(request):
    subjects = Subject.objects.all()
    lst = []
    for subject in subjects:
        if str(subject.subject_owner) == str(request.user):
            print(subject.id)
            lst.append(subject)
    if request.method != 'POST':
        form = userCurrentSelectedSubjects()
    else:
        form = userCurrentSelectedSubjects(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.subject_selection_owner = request.user
            new_form.save()
            return redirect('templateCreation')
    context = {'form': form,'subjects':lst}
    return render(request, "DockMaker/subjectselection.html", context)

@login_required
def templateCreation(request):
    subject_name = UserCurrentSelectedSubjects.objects.all()

    current_selected_subject = ''
    for subject in subject_name:
        if subject.subject_selection_owner == request.user:
            current_selected_subject = subject.selected_subject
            subject.delete()

    subject = Subject.objects.all()
    lst = list()
    for usersubject in subject:
        if str(usersubject.subject_owner) == str(request.user) and str(usersubject.subject_name) == str(
                current_selected_subject):
            lst.append(usersubject)

    experiments = Experiments.objects.all()
    experimentList = list()
    for experiment in experiments:
        if str(experiment.experiment_owner) == str(request.user) and str(experiment.experiment_name) == str(
                current_selected_subject):
            experimentList.append(experiment)
    content = list()
    con = list()
    doc1 = DocxTemplate(r'DocMaker/static/docfiles/Template_4.docx')
    path = "/DocMaker/static"
    for i in experimentList:
        d1, d2 = {}, {}
        print(f'Experiment number is : {i.experiment_number}')
        d1['Eno'] = i.experiment_number
        d1['exp'] = i.aim
        print(f'aim is : {i.aim}')
        d1['date'] = f'{i.timestamp}'[:10]
        print(f'date is : {i.timestamp}')
        d2['exp'] = i.experiment_number
        print(i.imageURL)
        d2['aim'] = i.aim
        d2['source_code'] = i.source_code
        if i.imageURL !='':
            d2['imageURL'] = InlineImage(doc1,f"DocMaker/static{i.imageURL}",width=Mm(107.1), height=Mm(111))
        d2['page_break'] = R('\f')
        content.append(d1)
        con.append(d2)

    # con = {
    #     'con': [{'exp': 1, 'aim': 'First', 'img': InlineImage(doc1, "D:\IMG.JPG", width=Mm(107.1), height=Mm(111)), },
    #             {'exp': 2, 'aim': 'Second', 'name': 'Wow1'}],
    #     'page_break': 'page break:'}
    # doc1.render(con)

    context = {"subject_name": lst[0].subject_name,
               "semester": lst[0].semester,
               "subject_faculty": lst[0].subject_faculty,
               "subject_owner": lst[0].subject_owner,
               "roll_no": lst[0].roll_no,
               "content": content,
               "con": con,


               }



    doc1.render(context,autoescape=True)
    # print(f"DocMaker/static{i.imageURL}")

    doc1.save(f'DocMaker/static/docfiles/{request.user}.docx')




    file_path = f'DocMaker/static/docfiles/{request.user}.docx'
    FilePointer = open(file_path,"rb")
    response = HttpResponse(FilePointer,content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = f'attachment; filename={request.user}.docx'




    if os.path.isfile(file_path):
        os.remove(file_path)
        print("success")
    else:
        print("File doesn't exists!")

    return response
