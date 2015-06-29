# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls2', '0003_auto_20150625_1302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='rating_a',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question_rating',
            new_name='rating',
        ),
    ]
