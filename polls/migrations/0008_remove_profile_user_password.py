# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_profile_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user_password',
        ),
    ]
