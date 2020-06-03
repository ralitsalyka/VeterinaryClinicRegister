from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from django.urls import reverse
from django import forms
from clinic.models import Procedure


def list(request):
    return render(request, 'procedures/list.html', {'procedures': Procedure.objects.all()})


def detail(request, procedure_id):
    procedure = get_object_or_404(Procedure, id=procedure_id)
    return render(request, 'procedures/detail.html', {'procedures': procedure})
