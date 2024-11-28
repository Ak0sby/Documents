from django.contrib import admin
from .models import *

# Бардык моделдерди каттоо
@admin.register(Spravki)
class SpravkiAdmin(admin.ModelAdmin):
    list_display = ('id', 'value')  # Поляңызды ылайыкташтырыңыз


@admin.register(PostCPGU)
class PostCPGUAdmin(admin.ModelAdmin):
    list_display = ('id', 'value')


@admin.register(TrebMil)
class TrebMilAdmin(admin.ModelAdmin):
    list_display = ('id', 'value')


@admin.register(VLKart)
class VLKartAdmin(admin.ModelAdmin):
    list_display = ('id', 'value')


@admin.register(Aktual)
class AktualAdmin(admin.ModelAdmin):
    list_display = ('id', 'value')


@admin.register(Akt_SUD)
class AktSUDAdmin(admin.ModelAdmin):
    list_display = ('id', 'value')


@admin.register(Post_prеkr)
class PostPrekrAdmin(admin.ModelAdmin):
    list_display = ('id', 'value')


@admin.register(Post_ad)
class PostAdAdmin(admin.ModelAdmin):
    list_display = ('id', 'value')


@admin.register(Istreb)
class IstrebAdmin(admin.ModelAdmin):
    list_display = ('id', 'value')

