from django.shortcuts import render, get_object_or_404, redirect
from .models import Entry
from .forms import EntryForm


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


def new_entry(request):
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.author = request.user
            entry.save()
            return redirect('entry_detail', entry_id=entry.id)
    context = {'form': form}
    return render(request, 'diary/new_entry.html', context)
