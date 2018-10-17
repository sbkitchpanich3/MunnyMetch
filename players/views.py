#from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import BetForm
from accounts.models import Profile

def index(request):
	return HttpResponse("<h1>test</h1>")

def betadd(request):
	 
	profile_instance = Profile.objects.get(user=request.user)

	if request.method == 'POST':

		bet_form = BetForm(request.POST)

		if bet_form.is_valid():

			profile_instance.munny = profile_instance.munny + bet_form.cleaned_data['bet']
			profile_instance.save()

			return HttpResponseRedirect(reverse('index'))

		else:
			return HttpResponseRedirect(reverse('index'))
			
def betminus(request):
	
	profile_instance = Profile.objects.get(user=request.user)

	if request.method == 'POST':

		bet_form = BetForm(request.POST)

		if bet_form.is_valid():

			profile_instance.munny = profile_instance.munny - bet_form.cleaned_data['bet']
			profile_instance.save()

			return HttpResponseRedirect(reverse('index'))

		else:
			return HttpResponseRedirect(reverse('index'))

