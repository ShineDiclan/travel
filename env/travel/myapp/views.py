from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def Destination(request):
    return render(request,'Destination.html')
def About(request):
    return render(request,'About.html')
def Contact(request):
    return render(request,'Contact.html')
def Booking(request):
    return render(request,'Booking.html')
