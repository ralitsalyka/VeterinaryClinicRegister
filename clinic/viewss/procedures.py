from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from django.urls import reverse
from django import forms
from clinic.models import Procedure, Animal, User


def list(request):
    current_user = request.user.id
    return render(request, 'procedures/list.html', {'procedures': Procedure.objects.filter(owner=current_user)})


def detail(request, procedure_id):
    procedure = get_object_or_404(Procedure, id=procedure_id)
    return render(request, 'procedures/detail.html', {'procedure': procedure})


class ProcedureForm(forms.ModelForm):
    class Meta:
        model = Procedure
        fields = ('name', 'animal_name', 'description', 'start_date', 'end_date', 'information')


def add_new_procedure(request):
    if request.method == "POST":
        data = request.POST
        form = ProcedureForm(data=data)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            animal_name = form.cleaned_data.get('animal_name')
            description = form.cleaned_data.get('description')
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
            information = form.cleaned_data.get('information')
            current_user = request.user
            owner = current_user
            new = Procedure(name=name, animal_name=animal_name, owner=owner, description=description, start_date=start_date, end_date=end_date, information=information)
            new.save()
            return redirect(reverse('clinic:procedures:list'))
        else:
            return render(request, 'procedures/create.html', {'form': form})
    else:
        form = ProcedureForm()
        return render(request, 'procedures/create.html', {'form': form})


def edit_procedure(request, procedure_id):
    procedure = Procedure.objects.get(id=procedure_id)
    if request.method == 'POST':
        form = ProcedureForm(data=request.POST, instance=procedure)
        if form.is_valid():
            form.save()
            return redirect(reverse('clinic:procedures:list'))
        else:
            return render(request, 'procedures/edit.html', {'procedure': procedure, 'form': form})
    else:
        form = ProcedureForm()
        return render(request, 'procedures/edit.html', {'procedure': procedure, 'form': form})


def delete_procedure(request, procedure_id):
    if request.method == 'POST':
        Procedure.objects.get(id=procedure_id).delete()
    return redirect(reverse('clinic:procedures:list'))
