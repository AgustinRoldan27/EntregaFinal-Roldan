from django.shortcuts import render, get_object_or_404, redirect
from .models import Page
from .forms import PageForm  # Necesitaremos crear este formulario
from django.contrib.auth.decorators import login_required

def page_list(request):
    page_list = Page.objects.all()
    return render(request, 'pages/page_list.html', {'page_list': page_list})

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'pages/page_detail.html', {'page': page})

@login_required
def page_edit(request, slug):
    page = get_object_or_404(Page, slug=slug)
    if request.method == 'POST':
        form = PageForm(request.POST, instance=page)
        if form.is_valid():
            form.save()
            return redirect('pages:page_detail', slug=page.slug)  # Redirigir al detalle
    else:
        form = PageForm(instance=page)
    return render(request, 'pages/page_edit.html', {'form': form, 'page': page})

@login_required
def page_delete(request, slug):
    page = get_object_or_404(Page, slug=slug)
    if request.method == 'POST':
        page.delete()
        return redirect('pages:page_list')  # Redirigir a la lista
    return render(request, 'pages/page_confirm_delete.html', {'page': page})

@login_required
def page_create(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pages:page_list')
    else:
        form = PageForm()
    return render(request, 'pages/page_create.html', {'form': form})