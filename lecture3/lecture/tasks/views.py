from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

class NewTask(forms.Form):
    task = forms.CharField(label="new task")

def index(request):
    tasks_key = "tasks_list"  # A string key to store the tasks list in the session

    # Retrieve the tasks list from the session or initialize it to an empty list
    tasks = request.session.get(tasks_key, [])

    return render(request, "tasks/index.html", {"tasks": tasks})

def add(request):
    tasks_key = "tasks_list"  # A string key to store the tasks list in the session

    if request.method == "POST":
        form = NewTask(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]

            # Retrieve the tasks list from the session or initialize it to an empty list
            tasks = request.session.get(tasks_key, [])
            request.session["tasks"] += tasks

            # Store the updated tasks list back to the session
            request.session[tasks_key] = tasks

            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {"form": form})
        
    return render(request, "tasks/add.html", {"form": NewTask()})
