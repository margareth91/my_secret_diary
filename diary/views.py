from django.shortcuts import render, get_object_or_404
from .models import Entry


def index(request):
    return render(request, 'diary/index.html', {})


def entry_list(request):
    entries = Entry.objects.order_by('-created_date')
    context = {'entries': entries}
    return render(request, 'diary/entry_list.html', context)


def entry_detail(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id)
    context = {'entry': entry}
    return render(request, 'diary/entry_detail.html', context)
