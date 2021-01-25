# -*- coding: utf-8 -*-
from django.shortcuts import render
from .screenshot import screenshot
from pyvirtualdisplay import Display
from selenium import webdriver




def home(request):
    print("girdim")
    screenshot.ekrangoruntusu1()
    return render(request,"home.html")

# Create your views here.
