from django.shortcuts import render
from django.http import HttpResponse

def index(request) :
	return HttpResponse("<h2>HEYYY</h2>")

def detail(request,offer_id):
	return HttpResponse("<h2>details:"+str(offer_id)+ "</h2>")
