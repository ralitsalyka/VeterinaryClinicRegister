from django.contrib import admin

from clinic.models import Animal, Procedure, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email')


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'species', 'description', 'photo')


@admin.register(Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('name', 'animal_name', 'owner', 'description', 'start_date', 'end_date', 'information')
