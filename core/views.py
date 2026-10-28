from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Product, Enquiry

def home(request):
    featured = Product.objects.filter(is_active=True, is_featured=True)[:3]
    return render(request, 'core/home.html', {'featured': featured, 'product_count': Product.objects.filter(is_active=True).count()})
def products(request):
    category = request.GET.get('category','')
    q = request.GET.get('q','').strip()
    items = Product.objects.filter(is_active=True)
    if category: items = items.filter(category=category)
    if q: items = items.filter(Q(name__icontains=q)|Q(brand__icontains=q)|Q(description__icontains=q))
    return render(request, 'core/products.html', {'products': items, 'category':category, 'q':q, 'categories':Product.CATEGORY_CHOICES})
def calculator(request):
    return render(request, 'core/calculator.html')
def about(request): return render(request, 'core/about.html')
def privacy(request): return render(request, 'core/privacy.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name','').strip(); phone = request.POST.get('phone','').strip()
        if not name or not phone:
            messages.error(request, 'Please enter your name and phone number.')
        else:
            Enquiry.objects.create(name=name, phone=phone, email=request.POST.get('email','').strip(), city=request.POST.get('city','').strip(), property_type=request.POST.get('property_type','home'), monthly_bill=request.POST.get('monthly_bill') or None, message=request.POST.get('message','').strip())
            messages.success(request, 'Thank you! Your enquiry has been saved. The team can follow up after checking the admin dashboard.')
            return redirect('contact')
    return render(request, 'core/contact.html')
