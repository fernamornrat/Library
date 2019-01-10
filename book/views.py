from django.shortcuts import render, redirect, get_object_or_404
from book.forms import TestForm
from .models import Book

def home(request):
    book_list = Book.objects.all()
    form = TestForm()
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/home/')
    return render(request, 'home.html', {'form1': form,'book_list': book_list})    

def edit(request,pk):
    edit = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = TestForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
        return redirect('/home/', pk=edit.pk)
    else:
        form = TestForm(instance=edit)    
    return render(request, 'edit.html', {'form': form,'edit': edit})    
    
def delete(request, pk):
    dele = get_object_or_404(Book, pk=pk)
    dele_pk = dele.pk
    dele.delete()    
    return redirect('/home/',pk=dele_pk)    
   