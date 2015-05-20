# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20150510_2318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='autor',
            new_name='author',
        ),
    ]
