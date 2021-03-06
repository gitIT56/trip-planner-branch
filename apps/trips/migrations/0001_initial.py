# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-24 00:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255)),
                ('lng', models.FloatField()),
                ('lat', models.FloatField()),
                ('result', models.CharField(max_length=255)),
                ('imgref', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('likes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='trip',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips_planned', to='trips.User'),
        ),
        migrations.AddField(
            model_name='trip',
            name='attended_by',
            field=models.ManyToManyField(related_name='trips_attending', to='trips.User'),
        ),
        migrations.AddField(
            model_name='trip',
            name='invited',
            field=models.ManyToManyField(related_name='trips_invited_to', to='trips.User'),
        ),
        migrations.AddField(
            model_name='agenda',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agendas', to='trips.Trip'),
        ),
        migrations.AddField(
            model_name='activity',
            name='agenda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='trips.Agenda'),
        ),
    ]
