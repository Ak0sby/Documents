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
