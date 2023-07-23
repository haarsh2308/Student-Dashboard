from django.shortcuts import render, redirect
from . forms import *
from django.contrib import messages
from django.views import generic
from youtubesearchpython import VideosSearch
import wikipediaapi

# Create your views here.
def home(request):
    return render(request, "dashboard/home.html")

def notes(request):
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            notes = Notes(user=request.user, title=request.POST['title'],description=request.POST['description'])
            notes.save()
        messages.success(request,"Notes added Successfully.")    
    else:
        form = NotesForm()
    form = NotesForm()
    notes = Notes.objects.filter(user=request.user)
    context = {'notes': notes, 'form': form}
    return render(request, "dashboard/notes.html", context)

def delete_note(request,pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect('notes')

class notes_detail(generic.DetailView):
    model = Notes

def videos(request):
    if request.method == 'POST':
        form = dashboardform(request.POST)
        text = request.POST['text']
        video = VideosSearch(text,limit=10)
        result_list = []
        for i in video.result()['result']:
            result_dict = {
                'input': text,
                'title':i['title'],
                'duration':i['duration'],
                'thumbnail':i['thumbnails'][0]['url'],
                'channel':i['channel']['name'],
                'link':i['link'],
                'views':i['viewCount']['short'],
                'published':i['publishedTime']
                }
            desc = ''
            if i['descriptionSnippet']:
                for j in i['descriptionSnippet']:
                    desc += j['text']
            result_dict['description'] = desc
            result_list.append(result_dict)
            context={
                'form': form,
                'results': result_list
            }
        return render(request, "dashboard/videos.html",context)
    else:
        form = dashboardform()
    context={'form':form}
    return render(request, "dashboard/videos.html",context)

def todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            try:
                finished = request.POST['is_completed']
                if finished == 1:
                    finished = True
                else:
                    finished = False
            except:
                finished = False
            todos = Todo(user=request.user, title=request.POST['title'],is_completed=finished)
            todos.save()
        messages.success(request,"Todo added Successfully.")    
    else:
        form = TodoForm()
    todo = Todo.objects.filter(user=request.user)
    if len(todo)== 0:
        todos_done = True
    else:
        todos_done = False
    context={'todos': todo, 'form': form, 'todos_done': todos_done}
    return render(request,"dashboard/todo.html",context)

def delete_todo(request,pk=None):
    Todo.objects.get(id=pk).delete()
    return redirect('todo')

def update_todo(request,pk=None):
    todo = Todo.objects.get(id=pk)
    if todo.is_completed == True:
        todo.is_completed = False
    else:
        todo.is_completed = True
    todo.save()
    return redirect('todo')
    
def wikipedia(request):
    if request.method == 'POST':
        text = request.POST['text']
        form = dashboardform(request.POST)
        wiki = wikipediaapi.Wikipedia('text','en')
        search = wiki.page('text')
        context={
            'form': form,
            'title': search.title,
            'link': search.url,
            'details': search.summary
        }
        return render(request, "dashboard/wikipedia.html",context)
    else:
        form = dashboardform()
        context={'form':form}
    return render(request, "dashboard/wikipedia.html",context)