from django.shortcuts import render
from .forms import SubsciberForm
from products.models import *

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

def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_phones = products_images.filter(product__category__id=1)
    products_images_laptops = products_images.filter(product__category__id=2)
    return render (request, 'landing/home.html', locals())