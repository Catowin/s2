from django.shortcuts import render
from .forms import SubsciberForm

def landing(request):
    name= 'Cat'
    form = SubsciberForm(request.POST or None)
    if request.method=="POST" and form.is_valid():
        print(request.POST)
        #print(form.cleaned_data)
        #data= form.cleaned_data
        #print(data['name'])
        new_form=form.save("The form was saved")
    return render (request, 'landing/landing.html', locals())