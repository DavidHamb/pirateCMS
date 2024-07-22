#from django.http import HttpResponse
from django.shortcuts import render
from cms.models import Case

def welcome(request):
    return render(request, 'cms/welcome.html')

def cases_list(request):
    cases = Case.objects.all()
    return render(request, 'cms/cases_list.html', {'cases': cases})