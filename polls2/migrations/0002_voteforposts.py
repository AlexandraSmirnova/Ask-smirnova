# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoteForPosts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.IntegerField()),
                ('post', models.IntegerField(default=0)),
                ('p_type', models.IntegerField(default=0)),
                ('voter', models.ForeignKey(related_name='VoteForPost', to='polls2.Profile')),
            ],
        ),
    ]
