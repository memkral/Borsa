# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from .views import *
#from .views import * de d,yebilirsin

app_name="analiz" #başka bir uygulamada detail ile karışmasın diye linkler ,buraya app name atadık şimdi modele gidip bunu belirtcez absolute url ye

urlpatterns = [


    path("",home,name="home"),


]