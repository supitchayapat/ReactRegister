# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 19:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('marks', '0001_initial'),
        ('classtime', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduledSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime(2017, 9, 10, 0, 0), verbose_name='subject date')),
                ('class_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classtime.ClassTime', verbose_name='class time')),
                ('grade_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marks.GradeSubject')),
            ],
        ),
    ]
