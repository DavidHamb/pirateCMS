from django.shortcuts import render, redirect
from cms.models import Case, Service
from cms.forms import CaseForm, CaseUpdateForm, AddServiceForm
from django.contrib import messages
from datetime import date

def welcome(request):
    return render(request, 'cms/welcome.html')


def cases_list(request):
    cases = Case.objects.all()
    return render(request, 'cms/cases.html', {'cases': cases})


def case_detail(request, id):
    case = Case.objects.get(id=id)
    services = Service.objects.filter(linked_case=case.id)
    return render(request, 'cms/case_detail.html', {'case': case, 'services': services})


def case_create(request):
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            case = form.save()
            messages.add_message(request, messages.INFO, "A new target has been successfully created! You can now edit the details ...")
            return redirect('case-detail', case.id)
    else:
        form = CaseForm()

    return render(request, 'cms/case_create.html', {'form': form})


def case_update(request, id):
    case = Case.objects.get(id=id)

    if request.method == 'POST':
        form = CaseUpdateForm(request.POST, instance=case)
        if form.is_valid():
            case.last_update = date.today()
            case.save()
            form.save()
            messages.add_message(request, messages.INFO, "The target has been updated successfully ...")
            return redirect('case-detail', case.id)
    else:
        form = CaseUpdateForm(instance=case)

    return render (request, 'cms/case_update.html', {'form': form, 'case': case})


def case_delete(request, id):
    case = Case.objects.get(id=id)

    if request.method == 'POST':
        case.delete()
        messages.add_message(request, messages.INFO, "The target has been deleted !")
        return redirect('cases-list')
    
    return render(request, 'cms/case_delete.html', {'case': case})


def add_service(request, id):
    case = Case.objects.get(id=id)
    form = AddServiceForm()

    if request.method == 'POST':
        form = AddServiceForm(request.POST)
        if form.is_valid():
            # Save form data AND the linked case (as hidden value)
            temporary_completion = form.save(commit=False)
            temporary_completion.linked_case = case
            temporary_completion.save() 
            return redirect('case-detail', case.id)
    else:
        form = AddServiceForm()

    return render(request, 'cms/add_service.html', {'form': form, 'case': case}) 