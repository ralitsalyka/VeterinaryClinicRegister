from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy

from clinic.models import Animal


def list(request):
    return render(request, 'animals/list.html', {'animals': Animal.objects.all()})


def detail(request, animal_id):
    animal = get_object_or_404(Animal, animal_id=animal_id)
    return render(request, 'animals/detail.html', {'animals': animal})


class AnimalCreateView(CreateView):
    model = Animal
    fields = ['name', 'owner', 'species', 'description']
    template_name = 'animals/create.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('clinic:animals:detail', kwargs={'animal_id': self.object.animal_id})
