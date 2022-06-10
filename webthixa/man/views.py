from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def home(request):
	conference = models.Conference.objects.all()
	nameplate = models.Nameplate.objects.all()
	category = models.Category.objects.all()
	context = {	
		'conference': conference,
		'nameplate': nameplate,
		'category': category,
	}
	return render(request, 'man/home.html', context)

def conference(request, conference_id):
	conference = models.Conference.objects.get(id=conference_id)
	context = {
		'conference': conference,
	}
	return render(request, 'man/conference.html', context)

def nameplate(request, nameplate_id):
	nameplate = models.Nameplate.objects.get(id=nameplate_id)
	context = {
		'nameplate': nameplate,
	}
	return render(request, 'man/nameplate.html', context)

def category(request, category_id):
	category = models.Category.objects.get(id=category_id)
	nameplate = models.Nameplate.objects.all()
	context = {
		'category': category,
		'nameplate': nameplate,
	}
	return render(request, 'man/category.html', context)

def edit_conference(request, conference_id):
	conference = models.Conference.objects.get(id=conference_id)
	nameplate = models.Nameplate.objects.all()
	context = {
		'conference': conference,
		'nameplate': nameplate,
	}
	return render(request, 'man/edit_conference.html', context)

def edit_conference_view_location(request, conference_id):
	conference = set()
	add_nameplate = []
	unchoose_nameplate = []
	dem = 0
	if request.method == 'POST':
		nameplate_id = request.POST.getlist('nameplate')

		for nameplate in models.Nameplate.objects.all():
			confirm = False
			for nameplateId in nameplate_id:
				if nameplate.id == int(nameplateId):
					confirm = True
					break
				else:
					confirm = False

			if confirm == True:
				add_nameplate.append(nameplate)
				conference.add(nameplate.conference)
			else:
				unchoose_nameplate.append(nameplate)

	context = {
		'conference_id': int(conference_id),
		'add_nameplate': add_nameplate,
		'conference': conference,
		'nameplate_id': nameplate_id,
		'unchoose_nameplate': unchoose_nameplate,
	}
	return render(request, 'man/edit_conference_view_location.html', context)

def completed(request):
	if request.method == 'POST':
		conference_id = int(request.POST.get('conference_id'))
		add_nameplate_id = request.POST.getlist('add_nameplate')
		remove_nameplate_id = request.POST.getlist('remove_nameplate')

		conference = models.Conference.objects.get(id=conference_id)
		add_nameplate = []
		remove_nameplate = []

		# ADD NAMEPLATE TO CONFERENCE
		for nameplate_id in add_nameplate_id:
			nameplate = models.Nameplate.objects.get(id=int(nameplate_id))
			if nameplate.conference != conference:
				add_nameplate.append(nameplate)
				nameplate.conference = conference
				nameplate.save()

		# REMOVE NAMEPLATE FROM CONFERENCE
		for nameplate_id in remove_nameplate_id:
			nameplate = models.Nameplate.objects.get(id=int(nameplate_id))
			remove_nameplate.append(nameplate)
			nameplate.conference = None
			nameplate.save()

	context = {
		'conference': conference,
		'add_nameplate': add_nameplate,
		'remove_nameplate': remove_nameplate,
	}
	return render(request, 'man/completed.html', context)