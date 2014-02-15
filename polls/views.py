from django.shortcuts import render
from django.http import HttpResponse

def index(reguest):
	return HttpResponse("Hello, world. You're at the poll index.")
