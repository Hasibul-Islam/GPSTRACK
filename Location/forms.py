from django import forms
from .models import *

class gps_form(forms.ModelForm):
	

	class Meta():
		model = Gps

		fields = ['CarID','Latitude','Longitude']