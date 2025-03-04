from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User


class Docs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='docs')
    spravki = models.IntegerField(verbose_name="Справки", default=0, null=True, blank=True,validators=[MaxValueValidator(999), MinValueValidator(0)])
    postcpgu = models.IntegerField(verbose_name="ПОСТ  ЦПГУ", default=0, null=True, blank=True,validators=[MaxValueValidator(999), MinValueValidator(0)])
    trebmil = models.IntegerField(verbose_name="ТРЕБ МИЛ", default=0, null=True, blank=True, validators=[MaxValueValidator(999), MinValueValidator(0)])
    vlkart = models.IntegerField(verbose_name="ВЛИТИЯ КАРТ", default=0, null=True, blank=True, validators=[MaxValueValidator(999), MinValueValidator(0)])
    aktual = models.IntegerField(verbose_name="АКТУАЛ", default=0, null=True, blank=True, validators=[MaxValueValidator(999), MinValueValidator(0)])
    akt_sud = models.IntegerField(verbose_name="АКТ СУД РЕЕСТ", default=0, null=True, blank=True, validators=[MaxValueValidator(999), MinValueValidator(0)])
    postprekr = models.IntegerField(verbose_name="ПОСТ ПРЕКР", default=0, null=True, blank=True, validators=[MaxValueValidator(999), MinValueValidator(0)])
    postad = models.IntegerField(verbose_name="ПОСТ ОБЬЯВЛ", default=0, null=True, blank=True, validators=[MaxValueValidator(999), MinValueValidator(0)])
    istreb = models.IntegerField(verbose_name="ИСТРЕБОВАНИЕ", default=0, null=True, blank=True, validators=[MaxValueValidator(999), MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Docs for {self.user.username}"
