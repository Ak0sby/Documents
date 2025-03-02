# Generated by Django 5.1.3 on 2025-02-27 08:43

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagram_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user_permissions',
        ),
        migrations.AlterField(
            model_name='trebmil',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trebmil', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='aktual',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aktual', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='istreb',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='istreb', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='spravki',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vlkart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vlkart', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='postcpgu',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postspgu', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='postprekr',
            name='user',
        ),
        migrations.RemoveField(
            model_name='postad',
            name='user',
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
        migrations.CreateModel(
            name='Akt_SUD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)], verbose_name='АКТ СУД РЕЕСТ')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='akt_sud', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post_ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)], verbose_name='ПОСТ ОБЬЯВЛ')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_ad', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post_prеkr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)], verbose_name='ПОСТ ПРЕКР')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_prekr', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='AktSUD',
        ),
        migrations.DeleteModel(
            name='PostPrekr',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
        migrations.DeleteModel(
            name='PostAd',
        ),
    ]
