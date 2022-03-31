from django.shortcuts import render, redirect
from .models import Note

def index(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag = request.POST.get('tag')
        if tag is None:
            tag = 'none'
        note = Note(id, title, content, tag)
        note.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})


def destroy(request):  
    id = request.POST.get('id')
    note = Note.objects.get(id = id)  
    note.delete()  
    return redirect('index')

def edit(request, id):  
    note = Note.objects.get(id=id)  
    return render(request,'notes/edit.html', {'note':note}) 

def update(request,id):
    title = request.POST.get('titulo')
    content = request.POST.get('detalhes')
    tag = request.POST.get('tag')
    id = request.POST.get('id')
    Note.objects.filter(id=id).update(title=title,content=content,tag=tag)
    return redirect('index')

def pageTags(request):
    # Notes distintas por tags
    notes = Note.objects.all().values('tag').distinct()
    return render(request, 'notes/tags.html', {'notes':  notes})

def specificTag(request,tag):
    notes = Note.objects.filter(tag=tag)
    return render(request, 'notes/specificTag.html', {'notes':  notes})

def home(request):
    all_notes = Note.objects.all()
    return render(request, 'notes/index.html', {'notes': all_notes})