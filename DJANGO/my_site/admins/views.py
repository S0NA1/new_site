from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>HELLO<h1/>")


def main(request):
    return HttpResponse("<h1>NEW MAIN PAGE<h1/>")
