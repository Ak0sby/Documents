from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User


class Spravki(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports')
    value = models.IntegerField(
        verbose_name="Справки",
        default=0,
        null=True,
        blank=True,
        validators=[MaxValueValidator(999), MinValueValidator(0)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Справки: {self.value}"


class PostCPGU(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postspgu')
    value = models.IntegerField(
        verbose_name="ПОСТ  ЦПГУ",
        default=0,
        null=True,
        blank=True,
        validators=[MaxValueValidator(999), MinValueValidator(0)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Пост ЦПГУ: {self.value}"


class TrebMil(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trebmil')
    value = models.IntegerField(
        verbose_name="ТРЕБ МИЛ",
        default=0,
        null=True,
        blank=True,
        validators=[MaxValueValidator(999), MinValueValidator(0)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Требования милиции: {self.value}"


class VLKart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vlkart')
    value = models.IntegerField(
        verbose_name="ВЛИТИЯ КАРТ",
        default=0,
        null=True,
        blank=True,
        validators=[MaxValueValidator(999), MinValueValidator(0)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Влитие КАРТ: {self.value}"


class Aktual(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='aktual')
    value = models.IntegerField(
        verbose_name="АКТУАЛ",
        default=0,
        null=True,
        blank=True,
        validators=[MaxValueValidator(999), MinValueValidator(0)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"АКТУАЛ: {self.value}"


class Akt_SUD(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='akt_sud')
    value = models.IntegerField(
        verbose_name="АКТ СУД РЕЕСТ",
        default=0,
        null=True,
        blank=True,
        validators=[MaxValueValidator(999), MinValueValidator(0)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"АКТ СУД РЕЕСТ: {self.value}"


class Post_prеkr(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_prekr')
    value = models.IntegerField(
        verbose_name="ПОСТ ПРЕКР",
        default=0,
        null=True,
        blank=True,
        validators=[MaxValueValidator(999), MinValueValidator(0)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ПОСТ ПРЕКР: {self.value}"


class Post_ad(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_ad')
    value = models.IntegerField(
        verbose_name="ПОСТ ОБЬЯВЛ",
        default=0,
        null=True,
        blank=True,
        validators=[MaxValueValidator(999), MinValueValidator(0)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ПОСТ ОБЬВЛЕНИЕ: {self.value}"


class Istreb(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='istreb')
    value = models.IntegerField(
        verbose_name= "ИСТРЕБОВАНИЕ",
        default=0,
        null=True,
        blank=True,
        validators=[MaxValueValidator(999), MinValueValidator(0)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ИСТРЕБОВАНИЕ: {self.value}"
