from django.contrib import messages
from django.shortcuts import render, redirect
from community.models import Column, Event
from community.forms import ColumnForm, EventForm



def columns(request):
    column_qu = Column.objects.all().order_by('-pk')
    return render(
        request,
        'community/column.html',
        {
            'column_list': column_qu,
        })

def column_detail(request, pk):
    column = Column.objects.get(pk=pk)
    return render(request, "community/column_detail.html",{
        "columns": column,
    })


def column_new(request):
    if request.method == "GET":
        form = ColumnForm()
    else:
        form = ColumnForm(request.POST)
        if form.is_valid():
            column = form.save()
            return redirect(f"/community/column/{column.pk}/")

    return render(request, "community/column_new.html", {
        "form": form,
    })

def events(request):
    event_qu = Event.objects.all().order_by('-pk')
    return render(request, "community/event.html",
                  {
                      'event_list': event_qu,
                  })

def event_detail(request, pk):
    event = Event.objects.get(pk=pk)
    return render(request, "community/event_detail.html",
                  {
                      "events": event,
                  })


def event_new(request):
    if request.method == 'GET':
        form = EventForm()
    else:
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save() # ModelForm에서 지원
            return redirect(f"/community/event/{event.pk}/")
    return render(request, "community/event_new.html",
                  {
                      "form": form
                  })