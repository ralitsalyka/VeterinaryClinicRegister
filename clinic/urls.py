from django.urls import path, include
from clinic.viewss import index, animals, procedures


app_name = 'clinic'


animals_patterns = [
    path('', animals.list, name='list'),
    path('<int:animal_id>/', animals.list, name='list'),
    path('new/', animals.add_new_animal, name='create'),
]

procedures_patterns = [
    path('', procedures.list, name='list'),
]

urlpatterns = [
    path('', index, name='index'),
    path('animals/', include((animals_patterns, 'animals'))),
    path('procedures/', include((procedures_patterns, 'procedures'))),
]
