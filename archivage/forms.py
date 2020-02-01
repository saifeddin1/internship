from django import forms
from .models import Entreprise, Person, Formation, Marketing, Development


class EntrepriseForm(forms.ModelForm):




	class Meta:
		model = Entreprise
		fields = [
				'title','manager','tel1','address',
				'cadre','rib','description', 'formation',
				'marketing','development']


class PersonForm(forms.ModelForm):




	class Meta:
		model = Person
		fields = [
				'first_name','last_name','tel','level',
				'address','description', 'formation',
				'marketing','development']
