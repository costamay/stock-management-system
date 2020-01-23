# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-23 06:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('materials', '0001_initial'),
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pu_date', models.DateTimeField(auto_now_add=True)),
                ('qyt', models.FloatField()),
                ('price', models.FloatField()),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materials.Material')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplier.Supplier')),
            ],
            options={
                'ordering': ['-pu_date'],
            },
        ),
    ]
