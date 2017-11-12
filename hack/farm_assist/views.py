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
from PIL import Image
import numpy as np
import os
import random 
from sklearn.svm import *
# from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import train_test_split
import pickle


			# from sklearn.neural_network import MLPClassifier

# Create your views here.


def login_site(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(username = email, password = password)
		if user:
			login(request, user)
			return redirect('/farmer_homepage/')
		else:
			return redirect('/login/')

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

	


		user=User.objects.create(username=email,password=password)
		user.set_password(password)
		user.save()

		far = farmer.objects.create(name = name,number = phone1,email = email,street = street,location = location,city = city,state = state,landmark = landmark,pincode = pin_code,user_id = user)
		far.save()

	
      
		return redirect('/login/')
	else:
		return render(request,'reg_form.html')


def farmer_homepage(request):
	if request.user.is_authenticated():
		return render(request,'hospitalHome.html')
	else:
		return redirect('/login/')


def seeds(request):
	if request.user.is_authenticated():
		return render(request,'seeds.html')
	else:
		return redirect('/login/')


def fertilizer(request):
	if request.user.is_authenticated():
		return render(request,'fert.html')
	else:
		return redirect('/login/')


def discuss(request):
	if request.user.is_authenticated():
		return render(request,'discuss.html')
	else:
		return redirect('/login/')


def subs(request):
	if request.user.is_authenticated():
		return render(request,'subs.html')
	else:
		return redirect('/login/')

def discuss(request):
	if request.user.is_authenticated():
		return render(request,'discuss.html')
	else:
		return redirect('/login/')


def disease(request):
	if request.user.is_authenticated():
		if request.method == 'POST':
			image = request.FILES['image']
			print(image)





			indir = '/home/deep/Desktop/hack_infinity/HackInfinity/hack/cotton-good/cotton crop images _ Google Search/'
			x_train = []
			y_train = []
			for root, dirs, filenames in os.walk(indir):
			    print("ASsadasd")
			    for f in filenames:
			        basewidth = 300
			        img = Image.open(indir+f)
			        img = img.resize((300,300), Image.ANTIALIAS)
			        x = np.array(img)
			        x = x.reshape((-1))
			#         print(x)
			        x = x.tolist()
			        x_train.append(x)
			        y_train.append(1)
			# x_train = np.array(x_train)
			print(np.array(x_train).shape)


			indir = '/home/deep/Desktop/hack_infinity/HackInfinity/hack/cotton-bad/boll rot disease cotton images _ Google Search/'
			for root, dirs, filenames in os.walk(indir):
			    print("ASsadasd")
			    for f in filenames:
			        basewidth = 300
			        img = Image.open(indir+f)
			        img = img.resize((300,300), Image.ANTIALIAS)
			        x = np.array(img)
			        x = x.reshape((-1))
			#         print(x)
			        x = x.tolist()
			        x_train.append(x)
			        y_train.append(0)
			# x_train = np.array(x_train)
			print(np.array(x_train).shape)

			# x_train,y_train

			combined = list(zip(x_train,y_train))
			random.shuffle(combined)
			x_train[:] ,y_train[:] = zip(*combined)

			xx_train,xx_test,yy_train,yy_test = train_test_split(x_train,y_train,test_size = 0.2)
			len(yy_train)


			# clf = MLPClassifier()
			clf = KNeighborsClassifier()
			for i in xx_train:
			    if len(i) != 270000:
			        xx_train.remove(i)
			        yy_train.pop()
			xx_train = np.array(xx_train)
			yy_train = np.array(yy_train).reshape(-1,1)
			clf.fit(xx_train,yy_train)
			

			


			for i in xx_test:
				if len(i) != 270000:
					xx_test.remove(i)
					yy_test.pop()



			pred = clf.predict(xx_test)

			print(accuracy_score(yy_test,pred))


			image = Image.open(image)
			print(image)
			image = image.resize((300,300), Image.ANTIALIAS)
			x = np.array(image)
			x = x.reshape(1,-1)
			print(x)	

			pr = clf.predict(x)
			print(pr)
			return HttpResponse("qwes")	

		else:
			return render(request,'disease.html')
	else:
		return redirect('/login/')
