from django.http import HttpResponse
from django.shortcuts import render

from .models import Product

# Create your views here.
# Views to create: contacts, accessories, about, home

# Home page
def home_view(request):
    context = {
        
    }
    return render(request, 'website/index.html', context)

def contact_view(request):
    context = {
        
    }
    return render(request, 'website/contact.html', context)

def accessories_view(request):
    products = Product.objects.all()
    context = {
        'products':products,
    }
    return render(request, 'website/accessories.html', context)

def description_view(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise ('This product does not exist')
    
    return render(request, 'website/description.html', {'product' : product})
    
    