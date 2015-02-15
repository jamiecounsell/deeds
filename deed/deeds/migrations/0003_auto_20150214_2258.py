# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deeds', '0002_auto_20150214_2257'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deed',
            old_name='deed_paid_for',
            new_name='paid_for',
        ),
        migrations.RemoveField(
            model_name='deed',
            name='deeds_paid_by',
        ),
        migrations.AddField(
            model_name='deed',
            name='paid_by',
            field=models.ManyToManyField(related_name='paid_by_rel_+', null=True, to='deeds.Deed'),
            preserve_default=True,
        ),
    ]
