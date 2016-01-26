from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from crmapp.subscribers.forms import SubscriberForm
from crmapp.subscribers.models import Subscriber

# Create your views here.

def subscriber_new(request, template = 'subscribers/subscriber_new.html'):
	if request.method == 'POST':
		form = SubscriberForm(request.POST)
		if form.is_valid():
			# Unpack form values
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			email = form.cleaned_data['email']
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			# Create the user record
			user = User(username = username, email = email, first_name = first_name, last_name = last_name)
			user.set_password(password)
			user.save()
			# Create subscriber record
			address_one = form.cleaned_data['address_one']
			address_two = form.cleaned_data['address_two']
			city = form.cleaned_data['city']
			state = form.cleaned_data['state']
			sub = Subscriber(address_one = address_one, address_two = address_two, city = city, state = state, user_rec = user)
			sub.save()
			# Process payment (via Stripe)
			# Auto login the user
			return HttpResponseRedirect('/success/')
	else:
		form = SubscriberForm()

	return render(request, template, {'form' : form})