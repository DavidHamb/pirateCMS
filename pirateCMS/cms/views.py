from django.shortcuts import render, redirect
from cms.models import Case, Service, Methodology, Note
from cms.forms import CaseForm, CaseUpdateForm, AddServiceForm, UpdateServiceForm, MethodologyUpdateForm, AddNoteForm
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
    notes = Note.objects.filter(linked_case=case.id)
    notes = notes.order_by('-id').values()
    return render(request, 'cms/case_detail.html', {'case': case, 'services': services, 'notes': notes})


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

            def handling_temporary_completion(x):
                x.linked_case = case
                x.save() 
                case.last_update = date.today()
                case.save()

            # Save form data AND the linked case (as hidden value)
            temporary_completion = form.save(commit=False)
            if Methodology.objects.filter(related_port=temporary_completion.port).exists():
                methodology = Methodology.objects.get(related_port=temporary_completion.port)
                temporary_completion.linked_methodology = methodology 
                handling_temporary_completion(temporary_completion)
            # Creating an empty methodology (if doesn't exist yet) and binding it to new service 
            else:
                methodology = Methodology()
                methodology.related_port = temporary_completion.port
                methodology.save()
                handling_temporary_completion(temporary_completion)
                temporary_completion.linked_methodology = methodology
                temporary_completion.save()
            return redirect('case-detail', case.id)
    else:
        form = AddServiceForm()

    return render(request, 'cms/add_service.html', {'form': form, 'case': case}) 


def update_service(request, id):
    service = Service.objects.get(id=id)
    case = Case.objects.get(id=service.linked_case_id)

    if request.method == 'POST':
        form = UpdateServiceForm(request.POST, instance=service)

        if form.is_valid():
            case.last_update = date.today()
            case.save()
            form.save()
            messages.add_message(request, messages.INFO, "The service has been updated successfully ...")
            return redirect('case-detail', case.id)

    else:
        form = UpdateServiceForm(instance=service)

    return render (request, 'cms/update_service.html', {'form': form, 'service': service, 'case': case })


def delete_service(request, id):
    service = Service.objects.get(id=id)
    case = Case.objects.get(id=service.linked_case_id)

    if request.method == 'POST':
        case.last_update = date.today()
        case.save()
        service.delete()
        messages.add_message(request, messages.INFO, "The service has been deleted !")
        return redirect('case-detail', case.id)
    
    return render(request, 'cms/delete_service.html', {'service': service, 'case': case})


def methodologies_list(request):
    methodologies = Methodology.objects.all()
    return render(request, 'cms/methodologies.html', {'methodologies': methodologies})



def methodology_update(request, id):
    methodology = Methodology.objects.get(id=id)

    if request.method == 'POST':
        form = MethodologyUpdateForm(request.POST, instance=methodology)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "The method has been updated successfully ...")
            return redirect('methodologies-list') # TODO rediriger vers le détail

    else:
        form = MethodologyUpdateForm(instance=methodology)

    return render(request, 'cms/methodology_update.html', {'methodology': methodology, 'form': form})


def methodology_delete(request, id):
    methodology = Methodology.objects.get(id=id)

    if request.method == 'POST':
        methodology.delete()
        messages.add_message(request, messages.INFO, "The methodology has been deleted !")
        return redirect('methodologies-list')
    
    return render(request, 'cms/methodology_delete.html', {'methodology': methodology})


def methodology_detail(request, id):
    methodology = Methodology.objects.get(id=id)
    return render(request, 'cms/methodology_detail.html', {'methodology': methodology})


def add_note(request, id):
    case = Case.objects.get(id=id)
    form = AddNoteForm()

    if request.method == 'POST':
        form = AddNoteForm(request.POST)
        if form.is_valid():

            # Save form data AND the linked case (as hidden value)
            temporary_completion = form.save(commit=False)
            temporary_completion.linked_case = case
            temporary_completion.save()
            case.last_update = date.today()
            case.save()
            return redirect('case-detail', case.id)
    else:
        form = AddNoteForm()

    return render(request, 'cms/add_note.html', {'form': form, 'case': case}) 


def delete_note(request, id):
    note = Note.objects.get(id=id)
    case = Case.objects.get(id=note.linked_case_id)

    if request.method == 'POST':
        case.last_update = date.today()
        case.save()
        note.delete()
        messages.add_message(request, messages.INFO, "The note has been deleted !")
        return redirect('case-detail', case.id)
    
    return render(request, 'cms/delete_note.html', {'note': note, 'case': case})

def default_method(request):
    return render(request, 'cms/default_method.html')