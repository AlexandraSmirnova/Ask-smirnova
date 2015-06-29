# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20150625_1052'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.IntegerField(default=0)),
                ('user', models.ForeignKey(to='polls.Profile')),
            ],
        ),
        migrations.RemoveField(
            model_name='voteforposts',
            name='voter',
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='reiting_a',
            new_name='rating_a',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question_reiting',
            new_name='question_rating',
        ),
        migrations.DeleteModel(
            name='VoteForPosts',
        ),
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
