# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django import forms
from stats.models import User,Domain,Domain_stats,Company
import json
from django.http import HttpResponseForbidden


# Create your views here.

def index(request):
	class LoginForm(forms.Form):
		username = forms.CharField(label = 'username', required = True)
		password = forms.CharField(label = 'password', widget=forms.PasswordInput)
 	error = False
	logged_in = False
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			try:
				user = User.objects.get(username = username)
				if user.password == password:
					logged_in = True
					request.session['username'] = username
					return render(request,'index.html',context = {'logged_in':True,'username' : username})
				else:
					error = True
			except User.DoesNotExist:
				error = True
			else:
				error = True
	else:
		username = request.session.get('username','')
		if username != '':
			return render(request,'index.html',context = {'logged_in':True,'username' : username})
		form = LoginForm()
	return render(request,'index.html',context = {'logged_in':logged_in,'error':error,'form':form})

def logout(request):
	request.session['username'] = ''
	return redirect('/index/')

def get(request,pk):
	username = request.session.get('username','')
	if username == '':
		return HttpResponseForbidden()
	user = User.objects.get(username = username)
	try:
		domain = Domain.objects.get(pk = pk)
		return redirect('/api/Domain_stats/?format=json&&qname=%s' % domain.name)
		
	except Domain.DoesNotExist:
		return render(request,'response.html', context = {'error':True, 'error_body':"Domain with id = %s doesn't exist" % pk})
	
