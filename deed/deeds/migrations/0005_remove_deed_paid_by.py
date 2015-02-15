# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deeds', '0004_auto_20150214_2303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deed',
            name='paid_by',
        ),
    ]
