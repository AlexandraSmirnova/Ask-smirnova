# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('polls2', '0002_voteforposts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voteforposts',
            name='voter',
            field=models.ForeignKey(related_name='VoteForPost', to=settings.AUTH_USER_MODEL),
        ),
    ]
