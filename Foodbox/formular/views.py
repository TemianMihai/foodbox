from django.shortcuts import render,redirect
from .forms import FormularForm
# Create your views here.
def formular1(request):
    form = FormularForm(data=request.POST or None)
    errors = []
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'Loosing_weigth.html',{
                'form':form,
                'errors':errors
    })

def formular2(request):
    form = FormularForm(data=request.POST or None)
    errors = []
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'Balanced_eating.html',{
                'form':form,
                'errors':errors
    })

def formular3(request):
    form = FormularForm(data=request.POST or None)
    errors = []
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'Mass_building.html',{
                'form':form,
                'errors':errors
    })

def formular4(request):
    form = FormularForm(data=request.POST or None)
    errors = []
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'Sport_program.html',{
                'form':form,
                'errors':errors
    })

def formular5(request):
    form = FormularForm(data=request.POST or None)
    errors = []
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'Vegetarian Food.html',{
                'form':form,
                'errors':errors
    })