from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.contrib import admin
from django.contrib.auth.models import User


class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'last_name', 'is_staff', 'is_superuser')
    search_fields = ('username', 'last_name')
    list_filter = ('is_superuser', 'is_staff')
    ordering = ('-id',)

# Мурун катталган User моделин кайра каттайбыз
admin.site.unregister(User)  # Биринчи мурунку каттоону өчүрөбүз
admin.site.register(User, CustomUserAdmin)  # Өзүбүздүн версияны каттайбыз


# Бардык моделдерди каттоо
@admin.register(Docs)
class DocsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'spravki', 'postcpgu', 'trebmil', 'vlkart', 'aktual', 'akt_sud', 'postprekr', 'postad', 'istreb','created_at')
    search_fields = ('user__username',)  # user атрибуту аркылуу издөөгө болот
    list_filter = ('created_at',)  # Маалыматтарды дата боюнча фильтрей алабыз
    ordering = ('-created_at',)  # Эң акыркы документтер биринчи көрсөтүлөт

