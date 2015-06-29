# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20150525_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='registration_date',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user_mail',
        ),
    ]
