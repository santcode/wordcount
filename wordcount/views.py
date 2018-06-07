"""
from django.http import HttpResponse
def home(request):
	return HttpResponse ('home')

def eggs(request):
	return HttpResponse ("<h1>Eggs are awesome</h1>")
"""

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	#return render(request,'home.html')
	return render(request,'home.html',{'hiter':'am here'})

def count(request):
	return render(request,'count.html')
