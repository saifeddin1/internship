from django.shortcuts import render
from .models import Entreprise, Person, Formation, Marketing, Development
from .forms import EntrepriseForm, PersonForm



def homepage(request):
	return render(request, 'home.html')




def add_entreprise(request):
	if request.method == 'POST':
		filled_form = EntrepriseForm(request.POST)
		if filled_form.is_valid():
			created_entreprise = filled_form.save()
			created_entreprise_pk = created_entreprise.id 
			filled_form = EntrepriseForm()
		return render(request, 'add_entreprise.html', {'entrepriseform':filled_form, 'created_entreprise_pk':created_entreprise_pk})
	else:

		form = EntrepriseForm()
		return render(request, 'add_entreprise.html', {'entrepriseform':form})




def add_client(request):
	if request.method == 'POST':
		filled_form = PersonForm(request.POST)
		if filled_form.is_valid():
			created_client = filled_form.save()
			created_client_pk = created_client.id 
			filled_form = PersonForm()
		return render(request, 'add_client.html', {'personform':filled_form, 'created_client_pk':created_client_pk})
	else:

		form = PersonForm()
		return render(request, 'add_client.html', {'personform':form})


