from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class BetForm(forms.Form):
	
	bet = forms.IntegerField(initial = 0)

	def clean_bet(self):
		cleanbet = self.cleaned_data['bet']

		# Check if bet is more than 0.
		if cleanbet > 0:
			return cleanbet

		else:
			raise ValidationError("Bet must be more than 0!")

class PlayerForm(forms.Form):

	player = forms.CharField(max_length = 100)
	#bet = forms.IntegerField(initial = 0)