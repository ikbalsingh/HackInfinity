# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import render,redirect
from django.http import HttpResponse

#from alpha_vantage.timeseries import TimeSeries
#from alpha_vantage.globalstockquotes import GlobalStockQuotes
import json

from .models import *

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import logout as auth_logout

from django.http import JsonResponse
# Create your views here.


def login_site(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(username = email, password = password)
		if user:
			login(request, user)
			return HttpResponse('login')
		else:
			return render(request, 'login.html')

	else:	
		return render(request, 'login.html')
		


def register(request):
	if request.method == 'POST':

		name = request.POST['name']
		email = request.POST['email']
		phone1 = request.POST['phone1']
		street = request.POST['street']
		location = request.POST['location']
		landmark = request.POST['landmark']
		city = request.POST['city']
		state = request.POST['state']
		pin_code = request.POST['pin_code']
		password = request.POST['password']

	


		user=User.objects.create(username=email)
		user.set_password(password)
		user.save()

		far = farmer.objects.create(name = name,number = phone1,email = email,street = street,location = location,city = city,state = state,landmark = landmark,pincode = pin_code,user_id = user)
		far.save()

	
      
		return HttpResponse('Check your mail box to confirm')
	else:
		return render(request,'reg_form.html')
