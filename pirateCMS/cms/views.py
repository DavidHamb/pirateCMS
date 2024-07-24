from django.shortcuts import render, redirect
from cms.models import Case
from cms.forms import CaseForm

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
        form = CaseForm(request.POST)
        if form.is_valid():
            case = form.save()
            return redirect('case-detail', case.id)
    else:
        form = CaseForm()

    return render(request, 'cms/case_create.html', {'form': form})

def case_update(request, id):
    case = Case.objects.get(id=id)

    if request.method == 'POST':
        form = CaseForm(request.POST, instance=case)
        if form.is_valid():
            form.save()
            return redirect('case-detail', case.id)
    else:
        form = CaseForm(instance=case)

    return render (request, 'cms/case_update.html', {'form': form})

def case_delete(request, id):
    case = Case.objects.get(id=id)

    if request.method == 'POST':
        case.delete()
        return redirect('cases-list')
    
    return render(request, 'cms/case_delete.html', {'case': case})