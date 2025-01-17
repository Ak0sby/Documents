from django.contrib import admin
from .models import *

# Бардык моделдерди каттоо
@admin.register(Spravki)
class SpravkiAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'user')  # user – логинди коштук


@admin.register(PostCPGU)
class PostCPGUAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'user')  # user – логинди коштук


@admin.register(TrebMil)
class TrebMilAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'user')  # user – логинди коштук


@admin.register(VLKart)
class VLKartAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'user')  # user – логинди коштук


@admin.register(Aktual)
class AktualAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'user')  # user – логинди коштук


@admin.register(Akt_SUD)
class AktSUDAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'user')  # user – логинди коштук


@admin.register(Post_prеkr)
class PostPrekrAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'user')  # user – логинди коштук


@admin.register(Post_ad)
class PostAdAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'user')  # user – логинди коштук


@admin.register(Istreb)
class IstrebAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'user')  # user – логинди коштук
