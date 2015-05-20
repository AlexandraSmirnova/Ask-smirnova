# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer_text', models.TextField(max_length=400)),
                ('pub_date', models.DateTimeField()),
                ('reiting_a', models.IntegerField(default=0)),
                ('flag', models.NullBooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=100)),
                ('user_password', models.CharField(default=123, max_length=100)),
                ('user_mail', models.EmailField(max_length=100)),
                ('user_reiting', models.IntegerField(default=0)),
                ('registration_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_title', models.CharField(max_length=100)),
                ('question_text', models.TextField(max_length=400)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('question_reiting', models.IntegerField(default=0)),
                ('autor', models.ForeignKey(default=1, to='polls.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(to='polls.Tag'),
        ),
        migrations.AddField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(to='polls.Profile'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(default=1, to='polls.Question'),
        ),
    ]
