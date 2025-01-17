# Generated by Django 5.1.3 on 2025-01-17 10:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagram_app', '0002_alter_akt_sud_value_alter_aktual_value_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='akt_sud',
            name='value',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)], verbose_name='АКТ СУД РЕЕСТ'),
        ),
        migrations.AlterField(
            model_name='aktual',
            name='value',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)], verbose_name='АКТУАЛ'),
        ),
        migrations.AlterField(
            model_name='istreb',
            name='value',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)], verbose_name='ИСТРЕБОВАНИЕ'),
        ),
        migrations.AlterField(
            model_name='post_ad',
            name='value',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)], verbose_name='ПОСТ ОБЬЯВЛ'),
        ),
        migrations.AlterField(
            model_name='post_prеkr',
            name='value',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)], verbose_name='ПОСТ ПРЕКР'),
        ),
        migrations.AlterField(
            model_name='postcpgu',
            name='value',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)], verbose_name='ПОСТ  ЦПГУ'),
        ),
        migrations.AlterField(
            model_name='spravki',
            name='value',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)], verbose_name='Справки'),
        ),
        migrations.AlterField(
            model_name='trebmil',
            name='value',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)], verbose_name='ТРЕБ МИЛ'),
        ),
        migrations.AlterField(
            model_name='vlkart',
            name='value',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)], verbose_name='ВЛИТИЯ КАРТ'),
        ),
    ]
