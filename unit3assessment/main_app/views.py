from django.shortcuts import render
from django.http import HttpResponse
from main_app.forms import WidgetForm
from .models import Widget
from .forms import WidgetForm
from django.shortcuts import render, redirect


def home(request):
    form = WidgetForm()
    allWidgets = Widget.objects.all()
    print(allWidgets)
    return render(request, 'home.html', {'form':form,'allWidgets': allWidgets})


def addwidget(request):
    form = WidgetForm(request.POST)
    if form.is_valid():
        new_widget = form.save(commit=False)
        new_widget.save()
        print("valid form")
    else: 
        print("invalid form")
    return redirect('home' )
    
def deleteWidget(request, widget_id):
    widget = Widget.objects.get(id=widget_id)
    widget.delete()
    print(widget)
    return redirect('home' )
    return render(request, 'home.html', {'widget': widget})
