from django.shortcuts import render
from .models import ContactUs, Bike, Color, Gallery


def home(request):
    gallery_images = Gallery.objects.all()
    context = {'gallery_images': gallery_images}
    return render(request, "index.html", context)
    

def contact(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('name')
        mobile_no = request.POST.get('mobile_no')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contactus = ContactUs(name=name, mobile_no=mobile_no, subject=subject, message=message)
        contactus.save()
        print('contact saved')
        
    return render(request, "page-contacts.html")

def shop(request):
    return render(request, "page-shop-grid.html")


def productDetails(request):
    return render(request, "page-shop-product-1.html")

def aboutUs(request):
    return render(request, "about-us.html")