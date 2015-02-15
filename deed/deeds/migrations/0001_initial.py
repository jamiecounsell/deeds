# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Deed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField(null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('paid', models.DateTimeField(null=True, blank=True)),
                ('lat', models.CharField(max_length=100, null=True, blank=True)),
                ('lon', models.CharField(max_length=100, null=True, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('deed_paid_for', models.ForeignKey(related_name='payment_deeds_for', to='deeds.Deed')),
                ('deeds_paid_by', models.ManyToManyField(related_name='payment_deeds_by', to='deeds.Deed')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
