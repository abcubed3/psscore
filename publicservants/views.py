from django.shortcuts import render, render_to_response, RequestContext

from .forms import PublicServantForm
# Create your views here.


def home(request):
    
    form = PublicServantForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        
    return render_to_response("index.html", locals(), context_instance=RequestContext(request))
