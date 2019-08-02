from django.shortcuts import render
from django.template import loader

from .forms import PoemForm

def index(request):
    poem = None
    title = None
    if request.method == 'POST':
        form = PoemForm(request.POST)
        if form.is_valid():
            seed = title = form.cleaned_data['keyword']
            poem = [' '.join([seed] * 8),
                    ' '.join([seed] * 8),
                    ' '.join([seed] * 5),
                    ' '.join([seed] * 5),
                    ' '.join([seed] * 8),]
    else:
        form = PoemForm()

    return render(request, 'poetix/index.html',
                  {'form': form, 'poem': poem, 'title': title})
