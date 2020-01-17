from django.shortcuts import render
from .models import Entreprise, Person, Formation, Marketing, Development

# Create your views here.

def homepage(request):
	entreprises = Entreprise.objects.all()
	persons = Person.objects.all()
	context = {
		'persons':persons,
		'entreprises':entreprises,
	}
	return render(request, 'home.html', context)