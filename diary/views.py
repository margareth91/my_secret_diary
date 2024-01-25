from django.shortcuts import render
from .models import Entry


def index(request):
    return render(request, 'diary/index.html', {})


def entry_list(request):
    entries = Entry.objects.order_by('created_date')
    context = {'entries': entries}
    return render(request, 'diary/entry_list.html', context)
