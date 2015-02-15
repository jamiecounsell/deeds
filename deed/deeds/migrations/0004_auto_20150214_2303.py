# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deeds', '0003_auto_20150214_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deed',
            name='paid_by',
            field=models.ManyToManyField(related_name='paid_by_rel_+', null=True, to='deeds.Deed', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='deed',
            name='paid_for',
            field=models.ForeignKey(related_name='deed_deeds_for', blank=True, to='deeds.Deed', null=True),
            preserve_default=True,
        ),
    ]
