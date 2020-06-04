from django.urls import path, include
from clinic.viewss import index, animals, procedures
from django.conf import settings
from django.conf .urls.static import static

app_name = 'clinic'


animals_patterns = [
    path('', animals.list, name='list'),
    path('<int:animal_id>/', animals.detail, name='detail'),
    path('new/', animals.add_new_animal, name='create'),
    path('edit/<int:animal_id>/', animals.edit_animal, name='edit'),
    path('delete/<int:animal_id>/', animals.delete_animal, name='delete'),
]

procedures_patterns = [
    path('', procedures.list, name='list'),
    path('<int:procedure_id>/', procedures.detail, name='detail'),
    path('new/', procedures.add_new_procedure, name='create'),
    path('edit/<int:procedure_id>/', procedures.edit_procedure, name='edit'),
    path('delete/<int:procedure_id>/', procedures.delete_procedure, name='delete'),
]

urlpatterns = [
    path('', index, name='index'),
    path('animals/', include((animals_patterns, 'animals'))),
    path('procedures/', include((procedures_patterns, 'procedures'))),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
