from django.contrib import messages
from django.shortcuts import render, redirect
from community.models import Column, Event
from community.forms import ColumnForm, EventForm
from django.views.generic import CreateView


def column(request):
    posts = Column.objects.all().order_by('-pk')
    return render(
        request,
        'community/column_index.html',
        {
            'post_list': posts,
        }
    )


def column_new(request, pk):
    post = Column.objects.get(pk=pk)

    return render(
        request,
        'community/column_new.html',
        {
            'post': post,
        }
    )


def column_form(request):
    if request.method == "GET":
        form = ColumnForm()
    else:
        form = ColumnForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect(post)
            # return redirect(f"/diary/{post.pk}/")

    return render(request, "community/column_form.html", {
        "form": form,
    })

def event_index(request):
    event = Event.objects.all().order_by('-pk')
    return render(request, "community/event_index.html",
                  {'event_qs': event,
                   })

def event_new(request):
    # print("request.method =", request.method)
    # print("request.POST =", request.POST)
    if request.method == 'GET':
        form = EventForm()
    else:
        form = EventForm(request.POST)
        if form.is_valid():
            # 유효성 검사에 통과한 값들이 저장된 dict
            # form.cleaned_data
            post = form.save() # ModelForm에서 지원
            # return redirect("/blog/")
            # return redirect(f'/blog/{post.pk}/")
            # return redirect(post.get_absolute_url())
            return redirect(post)
    return render(request, "community/event_form.html",{
        "form": form
    })

def event_post_page(request, pk):
    event = Event.objects.get(pk=pk)

    if request.method == 'POST':
        event.delete()
        return redirect("/event/")

    return render(request, "community/event_new.html",{
        "event_qs": event,
    })
