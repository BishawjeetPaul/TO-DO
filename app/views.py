from django.http import HttpResponseRedirect
from django.shortcuts import render
from app.models import Article
from django.http import HttpResponseRedirect

# Create your views here.
def dashboard(request):
    return render(request, 'layouts/main.html')

def create(request):
    if request.method != 'POST':
        return render(request, 'create.html')
    else:
        title = request.POST.get('title')
        body = request.POST.get('body')
        status = request.POST.get('status')

        articles = Article.objects.create(
            title = title,
            body = body,
            status = status
        )
        articles.save()
        return HttpResponseRedirect("/create_list/")

def create_list(request):
    articles = Article.objects.all()
    return render(request, 'create_list.html',{"articles": articles})

def task_details(request, pk):
    article = Article.objects.get(id=pk)
    return render(request, 'show_task.html', {"article": article})

def active_task(request):
    actives = Article.objects.filter(status='Active Task')
    return render(request, 'active_task.html', {"actives": actives})

def assigned_task(request):
    assigned = Article.objects.filter(status='Assigned to me')
    return render(request, 'assigned_task.html', {"assigned": assigned})

def complete_task(request):
    completed = Article.objects.filter(status='Completed')
    return render(request, 'complete_task.html', {"completed": completed})

def upcoming_task(request):
    upcoming = Article.objects.filter(status='Upcoming')
    return render(request, 'upcoming_task.html', {"upcoming": upcoming})

def overdue_task(request):
    overdue = Article.objects.filter(status='Overdue')
    return render(request, 'overdue_task.html', {"overdue": overdue})

def edit_task(request, pk):
    if request.method != 'POST':
        task = Article.objects.get(id=pk)
        return render(request, 'edit_task.html', {"task": task, "pk": pk})
    else:
        pk = request.POST.get('pk')
        titl = request.POST.get('titl')
        bod = request.POST.get('bod')
        statu = request.POST.get('statu')

        task = Article.objects.get(id=pk)
        task.title = titl
        task.body = bod
        task.status = statu
        task.save()
        return HttpResponseRedirect("/create_list/")

def delete_task(request, pk):
    task = Article.objects.get(id=pk)
    task.delete()
    return HttpResponseRedirect("/create_list/")
