#from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import BetForm, PlayerForm
from accounts.models import Profile
from .models import Challenge

#TODO: Get player_by_id out to the template somehow
	   # Separate bet form names for error testing?

class ListView(generic.ListView):
	template_name = 'challengelist.html'
	context_object_name = 'challenges'

	# Get set of challenges where either you're the sender or receiver.
	def get_queryset(self):
		result = Challenge.objects.filter(sender=self.request.user) | Challenge.objects.filter(receiver=self.request.user)
		return result

def index(request):
	return HttpResponse("<h1>test</h1>")

def betadd(request):
	#Get the Profile of the currently logged in user.
	profile_instance = Profile.objects.get(user=request.user)

	if request.method == 'POST':

		bet_form = BetForm(request.POST)

		if bet_form.is_valid():
			#Take the player's current munny, plus the bet money from it, and save to database.
			profile_instance.munny = profile_instance.munny + bet_form.cleaned_data['bet']
			profile_instance.save()
			#Rendering the same page, but passing in the bet form as context to get it to display on page.
			return render(request, 'index.html', {'bet_form': bet_form})

		else:
			return render(request, 'index.html', {'bet_form': bet_form})

def betminus(request):
	#Get the Profile of the currently logged in user.
	profile_instance = Profile.objects.get(user=request.user)

	if request.method == 'POST':

		bet_form = BetForm(request.POST)

		if bet_form.is_valid():
			#Take the player's current munny, minus the bet money from it, and save to database.
			profile_instance.munny = profile_instance.munny - bet_form.cleaned_data['bet']
			profile_instance.save()
			#Rendering the same page, but passing in the bet form as context to get it to display on page.
			return render(request, 'index.html', {'bet_form': bet_form})

		else:
			return render(request, 'index.html', {'bet_form': bet_form})

def challenge(request):
# User works by calling get(username='')

	if request.method == 'GET':
	
		player_form = PlayerForm()
		return render(request, 'challenge.html', {'player_form': player_form})

	else:

		player_form = PlayerForm()
		return render(request, 'challenge.html', {'player_form': player_form})

#old code that worked, its now in the confirm view.

		# current_player = Profile.objects.get(user=request.user)
		# player_form = PlayerForm(request.POST)

		# if player_form.is_valid():
			
		# 	name = player_form.cleaned_data['player']
		# 	bet = player_form.cleaned_data['bet']
			
		# 	try:
		# 		player_object = User.objects.get(username__iexact=name)
		# 	except User.DoesNotExist:
		# 		return HttpResponse("My dude that person isn't a player!")
			
		# 	ky = player_object.id
			
		# 	player_by_id = Profile.objects.get(user=ky)
		# 	return render(request, 'challenge.html', {'player_form': player_form})

		# else:

		# 	player_form = PlayerForm()
		# 	return render(request, 'challenge.html', {'player_form': player_form})

def confirm(request):
# User works by calling get(username='')

	if request.method == 'POST':
		#get the Profile of the currently logged in user.
		current_player = Profile.objects.get(user=request.user)
		player_form = PlayerForm(request.POST)

		if player_form.is_valid():
			# ['player'] field has to match what's in the index template's form name.  BULLSHIT!
			# This is responsible for getting the POST data btw.
			# name is getting the clean version of the player attribute from the PlayerForm.
			name = player_form.cleaned_data['player']
			bet = player_form.cleaned_data['bet']
			# player_object grabs the user from the User class using the username provided by the POST data.
			try:
				player_object = User.objects.get(username__iexact=name)
			except User.DoesNotExist:
				return HttpResponse("My dude that person isn't a player!")
			# Getting the primary key of the pulled user.
			ky = player_object.id
			# I can't pass in the user directly for some fucking reason so it's gotta be done this way GRRR D:<
			player_by_id = Profile.objects.get(user=ky)
			return render(request, 'confirm.html', {'player_form': player_form})

		else:

			player_form = PlayerForm()
			return render(request, 'confirm.html', {'player_form': player_form})

	else:

		player_form = PlayerForm()
		return render(request, 'confirm.html', {'player_form': player_form})

def confirm2(request):
	#current_player = Profile.objects.get(user=request.user.id)
	player_form = PlayerForm(request.POST)

	if request.method == 'POST':
		#get the Profile of the currently logged in user.

		if player_form.is_valid():
			# ['player'] field has to match what's in the index template's form name.  BULLSHIT!
			# This is responsible for getting the POST data btw.
			# name is getting the clean version of the player attribute from the PlayerForm.
			name = player_form.cleaned_data['player']
			betAmount = player_form.cleaned_data['bet']
			# player_object grabs the user from the User class using the username provided by the POST data.
			try:
				player_object = User.objects.get(username__iexact=name)
			except User.DoesNotExist:
				return HttpResponse("My dude that person isn't a player!")
			# Create a new Challenge object with a user object
			newChallenge = Challenge(sender=request.user, receiver=player_object, bet=betAmount, status=0, p1result=None, p2result=None)
			newChallenge.save()
			return render(request, 'confirm.html', {'player_form': player_form})

		else:

			player_form = PlayerForm()
			return render(request, 'confirm.html', {'player_form': player_form})

	else:

		player_form = PlayerForm()
		return render(request, 'confirm.html', {'player_form': player_form})