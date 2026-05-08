from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProductForm
from .models import Product

def dashboard(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ProductForm()

    products = Product.objects.all().order_by('-id')
    return render(request, 'inventory/dashboard.html', {
        'form': form,
        'products': products
    })

def home(request):
    return render(request, 'inventory/index.html')