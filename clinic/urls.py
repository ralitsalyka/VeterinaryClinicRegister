from django.urls import path, include
from clinic.viewss import index


app_name = 'clinic'


urlpatterns = [
    path('', index, name='index')
]
