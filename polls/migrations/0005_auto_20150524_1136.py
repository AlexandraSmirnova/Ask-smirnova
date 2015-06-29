# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='likes',
            field=models.ManyToManyField(to='polls.Like'),
        ),
        migrations.AddField(
            model_name='question',
            name='likes',
            field=models.ManyToManyField(to='polls.Like'),
        ),
    ]
