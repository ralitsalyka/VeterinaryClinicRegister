from django.urls import path, include
from clinic.viewss import index, animals


app_name = 'clinic'


animals_patterns = [
    path('', animals.list, name='list'),
    path('<int:animal_id>/', animals.detail, name='detail'),
    path('new/', animals.AnimalCreateView.as_view(), name='create'),
]

urlpatterns = [
    path('', index, name='index'),
    path('animal/', animals.AnimalCreateView.as_view(), name="animal"),
]
