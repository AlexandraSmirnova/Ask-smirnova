# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20150511_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('positive', models.IntegerField(default=0)),
                ('negative', models.IntegerField(default=0)),
                ('user', models.ForeignKey(to='polls.Profile')),
            ],
        ),
    ]
