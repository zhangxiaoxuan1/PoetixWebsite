from django.shortcuts import render
from django.template import loader

from .forms import PoemForm

import sys
import os

# Change the directory to Poetix folder's directory
working_dir = '/Users/isaac/Desktop/Poetix/poetix/'

sys.path.append(working_dir)
from py_files.Limericks import Limerick_Generate

def index(request):
    poem = []
    title = None
    if request.method == 'POST':
        form = PoemForm(request.POST)
        os.chdir(working_dir)
        lg = Limerick_Generate(model_name='117M',load_poetic_vectors=False)
        if form.is_valid():
            seed = title = form.cleaned_data['keyword']
            generated_poem = lg.gen_poem_gpt("mary", "mary",
                       prompt_length=100, search_space=150, story_line=True,
                       default_templates=[['WHO', 'VBD', 'NNS', 'IN', 'DT', 'NN'],
                                          ['PRP', 'VBD', 'DT', 'NN'],
                                          ['IN', 'DT', 'JJ', 'NN'],
                                          ['CC', 'VBD', 'IN', 'DT', 'JJ', 'NN']
                                         ],
                       enforce_syllables = True, enforce_stress = True)
            for line in generated_poem:
                str = ' '.join(line)
                str[0] = str[0].toUpperCase()
                poem.append(str)
    else:
        form = PoemForm()

    return render(request, 'poetix/index.html',
                  {'form': form, 'poem': poem, 'title': title})
