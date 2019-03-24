from django.http import HttpResponse
from polls.api import QuesSerializer,ChoiceSerializer,QuesViewSet,ChoiceViewSet
from polls.models import Question, Choice, Track
from polls.forms import QuestionForm, ChoiceForm, TrackForm
from django.shortcuts import render, redirect

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def pollqn(request):

    if request.method == "POST":
        print("POST4")
        form = QuestionForm(request.POST)
        #print(form.cleaned_data['question_text'])
        print("POST3")
        if form.is_valid():
            print("POST1")
            try:
                form.save()
                print("POST2")
                return redirect('/polls/viewqn')
            except:
                pass
    else:
        print("GET")
        form = QuestionForm()
    return render(request,'indexqn.html',{'form':form})


def pollch(request):

    if request.method == "POST":
        print("POST4")
        form = ChoiceForm(request.POST)
        #print(form.cleaned_data['question_text'])
        print("POST3")
        if form.is_valid():
            print("POST1")
            try:
                form.save()
                print("POST2")
                return redirect('/polls/viewch')
            except:
                pass
    else:
        print("GET")
        form = ChoiceForm()
    return render(request,'indexch.html',{'form':form})


def polltr(request):

    if request.method == "POST":
        print("POST4")
        form = TrackForm(request.POST)
        #print(form.cleaned_data['question_text'])
        print("POST3")
        if form.is_valid():
            print("POST1")
            try:
                form.save()
                print("POST2")
                return redirect('/polls/viewtr')
            except:
                pass
    else:
        print("GET")
        form = TrackForm()
    return render(request,'indextr.html',{'form':form})


def QuesViewSet(request):
    polls = Question.objects.all()
    return render(request,"showqn.html",{'polls':polls})

def ChoiceViewSet(request):
    polls = Choice.objects.all()
    return render(request,"showch.html",{'polls':polls})
def TrackViewSet(request):
    polls = Track.objects.all()
    return render(request,"showtr.html",{'polls':polls})
def QnChViewSet(request):
    question = Question.objects.all()
    choice = Choice.objects.all()
    return render(request,"showqnch.html",{'choice':choice},{'question':question})

def editqn(request, id):
    form = Question.objects.get(id=id)
    return render(request,'editqn.html',{'form':form})
def editch(request, id):
    form = Choice.objects.get(id=id)
    return render(request,'editch.html', {'form':form})
def edittr(request, id):
    form = Track.objects.get(id=id)
    return render(request,'edittr.html', {'form':form})
def updateqn(request, id):
    polls = Question.objects.get(id=id)
    form = QuestionForm(request.POST, instance = polls)
    if form.is_valid():
        form.save()
        return redirect('/polls/viewqn')
    return render(request, 'editqn.html', {'form': form})

def updatech(request, id):
    polls = Choice.objects.get(id=id)
    print(polls)
    form = ChoiceForm(request.POST, instance = polls)
    print(form)
    if form.is_valid():
        print("valid")
        form.save()
        return redirect('/polls/viewch')
    return render(request, 'editch.html', {'form': form})

def updatetr(request, id):
    polls = Track.objects.get(id=id)
    form = TrackForm(request.POST, instance = polls)
    if form.is_valid():
        form.save()
        return redirect('/polls/viewtr')
    return render(request, 'edittr.html', {'form': form})

def destroyqn(request, id):
    Poll = Question.objects.get(id=id)
    Poll.delete()
    return redirect('/polls/viewqn')

def destroych(request, id):
    Poll = Choice.objects.get(id=id)
    Poll.delete()
    return redirect('/polls/viewch')
def destroytr(request, id):
    Poll = Track.objects.get(id=id)
    Poll.delete()
    return redirect('/polls/viewtr')
