from django.shortcuts import render, redirect
from cms.models import Case
from cms.forms import NewCaseForm

def welcome(request):
    return render(request, 'cms/welcome.html')

def cases_list(request):
    cases = Case.objects.all()
    return render(request, 'cms/cases.html', {'cases': cases})

def case_detail(request, id):
    case = Case.objects.get(id=id)
    return render(request, 'cms/case_detail.html', {'case': case})

def case_create(request):
    if request.method == 'POST':
        form = NewCaseForm(request.POST)
        if form.is_valid():
            case = form.save()
            return redirect('case-detail', case.id)
    else:
        form = NewCaseForm()

    return render(request, 'cms/case_create.html', {'form': form})