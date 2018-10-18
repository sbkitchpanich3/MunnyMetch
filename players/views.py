#from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import BetForm, PlayerForm
from accounts.models import Profile

#TODO: Test printing errors or request.user to a template

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

def challenge(request):
#User works by calling get(username='')

	if request.method == 'POST':

		player_form = PlayerForm(request.POST)

		if player_form.is_valid():
			#['player'] field has to match what's in the index template's form name.  BULLSHIT!
			name = player_form.cleaned_data['player']
			player_object = User.objects.get(username=name)
			ky = player_object.id
			#seems like this method works right meow?
			player_by_id = Profile.objects.get(user=ky)
			return HttpResponse(player_by_id)

		else:

			player_form = PlayerForm()
			return HttpResponseRedirect(reverse('index'))

