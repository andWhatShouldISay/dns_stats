# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Company(models.Model):
	#автоматически добавлен primary key

	name = models.TextField()

	def __str__(self):
		return self.name

class User(models.Model):
	#автоматически добавлен primary key 

	companyid = models.ForeignKey(Company, on_delete=models.CASCADE)
	username = models.CharField(max_length = 32, unique = True)
	email = models.CharField(max_length = 32)
	password = models.CharField(max_length = 32)

	def __str__(self):
		return self.username

class Domain(models.Model):
	#автоматически добавлен primary key
 
	companyid = models.ForeignKey(Company, on_delete=models.CASCADE)
	name = models.CharField(max_length = 32)

	def __str__(self):
		return self.name

class Domain_stats(models.Model):
	qname = models.CharField(max_length = 64)
	query_id = models.IntegerField()
	src_addr = models.CharField(max_length = 64)
	dst_addr = models.CharField(max_length = 64)
	src_port = models.IntegerField()
	dst_port = models.IntegerField()
	qr = models.BooleanField()
	do = models.BooleanField()
	rd = models.BooleanField()
	ra = models.BooleanField()
		
	def __str__(self):
		return self.qname

	class Meta:
		ordering = ['qr']


