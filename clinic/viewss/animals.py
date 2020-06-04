from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from django.urls import reverse
from django import forms
from clinic.models import Animal


def list(request):
    current_user = request.user
    return render(request, 'animals/list.html', {'animals': Animal.objects.filter(owner=current_user)})


def detail(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    return render(request, 'animals/detail.html', {'animals': animal})


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ('name', 'species', 'description', 'photo')


def add_new_animal(request):
    if request.method == "POST":
        data = request.POST
        form = AnimalForm(data=data)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            species = form.cleaned_data.get('species')
            description = form.cleaned_data.get('description')
            photo = form.cleaned_data.get('photo')
            current_user = request.user
            owner = current_user
            new = Animal(name=name, species=species, owner=owner, description=description, photo=photo)
            new.save()
            return redirect(reverse('clinic:animals:list'))
        else:
            return render(request, 'animals/create.html', {'form': form})
    else:
        form = AnimalForm()
        return render(request, 'animals/create.html', {'form': form})


def edit_animal(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    if request.method == 'POST':
        form = AnimalForm(data=request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect(reverse('clinic:animals:list'))
        else:
            return render(request, 'animals/edit.html', {'animal': animal, 'form': form})
    else:
        form = AnimalForm(initial={"name": animal.name, "species": animal.species, "description": animal.description, "photo": animal.photo })
        return render(request, 'animals/edit.html', {'animal': animal, 'form': form})


def delete_animal(request, animal_id):
    if request.method == 'POST':
        Animal.objects.get(id=animal_id).delete()
    return redirect(reverse('clinic:animals:list'))
