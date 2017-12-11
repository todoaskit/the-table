# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 17:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('session', '0008_auto_20171211_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPostProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.IntegerField(choices=[(None, '선택해주세요'), (0, '전혀 동의하지 않는다'), (1, '동의하지 않는다'), (2, '보통이다'), (1, '동의한다'), (1, '매우 동의한다')], help_text='세금을 내는 이상, 모든 공약은 비용이 든다. 따라서 나에게 이득이 되지 않은 공약은 나에게 손해다', verbose_name='설문 1')),
                ('q2', models.IntegerField(choices=[(None, '선택해주세요'), (0, '전혀 동의하지 않는다'), (1, '동의하지 않는다'), (2, '보통이다'), (1, '동의한다'), (1, '매우 동의한다')], help_text='나의 가족의 손해는 나의 손해다', verbose_name='설문 2')),
                ('q3', models.IntegerField(choices=[(None, '선택해주세요'), (0, '전혀 동의하지 않는다'), (1, '동의하지 않는다'), (2, '보통이다'), (1, '동의한다'), (1, '매우 동의한다')], help_text='우리 사회의 손해는 나의 손해다', verbose_name='설문 3')),
                ('q4', models.IntegerField(choices=[(None, '선택해주세요'), (0, '전혀 동의하지 않는다'), (1, '동의하지 않는다'), (2, '보통이다'), (1, '동의한다'), (1, '매우 동의한다')], help_text='자연의 손해는 나의 손해다', verbose_name='설문 4')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
