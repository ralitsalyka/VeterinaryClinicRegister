from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from django.urls import reverse
from django import forms
from clinic.models import Animal


def list(request):
    return render(request, 'animals/list.html', {'animals': Animal.objects.all()})


def detail(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    return render(request, 'animals/detail.html', {'animals': animal})


class CrouseForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ('name', 'species', 'description', 'photo')


def add_new_animal(request):
    if request.method == "POST":
        data = request.POST
        form = CrouseForm(data=data)
        if form.is_valid():
            new_animal = form.save()
            return redirect(reverse('clinic:animals:list'))
        else:
            return render(request, 'animals/create.html', {'form': form})
    else:
        form = CrouseForm()
        return render(request, 'animals/create.html', {'form': form})
