from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home_page_view(request):
	return render(request, 'website/home.html')

def about_page_view(request):
	return render(request, 'website/about.html')

def contacts_page_view(request):
	return render(request, 'website/contacts.html')