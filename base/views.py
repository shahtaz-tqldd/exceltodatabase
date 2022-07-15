from django.shortcuts import render
from .models import Person
from .resources import PersonResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse

# Create your views here.
def export(request):
	person_resource = PersonResource()
	dataset = person_resource.export()
	response = HttpResponse(dataset.xls, content_type = 'application/vnd.ms-excel')
	response['Content-Disposition'] = 'attachment; filename ="person.xls"'
	return response

def home(request):
	if request.method == 'POST':
		person_resource = PersonResource()
		dataset = Dataset()
		new_person = request.FILES['myfile']

		if not new_person.name.endswith('xlsx'):
			messages.info(request, 'wrong format')
			return render(request, 'upload.html')

		imported_data = dataset.load(new_person.read(), format='xlsx')
		for data in imported_data:
			value = Person(
				data[0],
				data[1],
				data[2],
				data[3],
				)
			value.save()
	context = {}
	return render(request, 'base/index.html', context)

def person(request):
	person = Person.objects.all()
	context = {'person': person}
	return render(request, 'base/persons.html', context)