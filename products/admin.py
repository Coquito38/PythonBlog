from django.contrib import admin
from users.models import User_profile
from products.models import  Contenido, Reseña, Platform

# Register your models here.
@admin.register(Contenido)
class Contenido_admin(admin.ModelAdmin):
    list_display = [
    'name'
    ,'category'
    ,'score'
    ,'modified_date'
    ,'created_date'
    ,'description'
    ,'image_url'
    ]

@admin.register(Reseña)
class Contenido_admin(admin.ModelAdmin):
    list_display = [
    'name'
    ,'puntaje'
    ,'body'
    ]

@admin.register(Platform)
class Platform_admin(admin.ModelAdmin):
    list_display = [
    'name'
    ,'description'
    ,'image_url'
    ]

@admin.register(User_profile)
class User_profile_admin(admin.ModelAdmin):
    list_display = [
    'user'
    ,'phone'
    ,'about'
    ,'image'
    ]
