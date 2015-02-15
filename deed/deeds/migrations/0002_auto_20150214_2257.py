# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deeds', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='deed_paid_for',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='deeds_paid_by',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.AddField(
            model_name='deed',
            name='deed_paid_for',
            field=models.ForeignKey(related_name='deed_deeds_for', to='deeds.Deed', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deed',
            name='deeds_paid_by',
            field=models.ManyToManyField(related_name='deeds_paid_by_rel_+', null=True, to='deeds.Deed'),
            preserve_default=True,
        ),
    ]
