# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0012_auto_20150618_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoteForPosts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.IntegerField()),
                ('post', models.IntegerField(default=0)),
                ('p_type', models.IntegerField(default=0)),
                ('voter', models.ForeignKey(related_name='VoteForPost', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='question',
            name='likes',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
