from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

# Create your views here.
def indexPage(request):
    return render(request, 'inventory/index.html')


def dashboardPage(request):
    submitted = False  

    if request.method == 'POST':
        form = ProductForm(request.POST)
        submitted = True

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = ProductForm()

    products = Product.objects.all()

    context = {
        'form': form,
        'products': products,
        'submitted': submitted,
    }

    return render(request, 'inventory/dashboard.html', context)