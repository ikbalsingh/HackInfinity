# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings



# Create your models here.

class farmer(models.Model):
	name = models.CharField(max_length=100)
	number = models.CharField(max_length=100)
	email = models.CharField(max_length=100,unique=True)
	street = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	landmark = models.CharField(max_length=100)
	pincode = models.CharField(max_length=100)
	user_id = models.ForeignKey(User)



	def __str__(self):
		return self.name
