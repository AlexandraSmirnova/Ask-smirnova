# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20150524_1136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='negative',
            new_name='state',
        ),
        migrations.RemoveField(
            model_name='like',
            name='positive',
        ),
    ]
