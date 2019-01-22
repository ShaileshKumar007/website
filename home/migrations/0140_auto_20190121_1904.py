# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-01-21 19:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0139_midpointinternfeedback_midpointmentorfeedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='midpointinternfeedback',
            name='mentor_response_frequency',
        ),
        migrations.RemoveField(
            model_name='midpointinternfeedback',
            name='mentor_response_time',
        ),
        migrations.RemoveField(
            model_name='midpointmentorfeedback',
            name='mentor_response_frequency',
        ),
        migrations.RemoveField(
            model_name='midpointmentorfeedback',
            name='mentor_response_time',
        ),
        migrations.AddField(
            model_name='midpointinternfeedback',
            name='mentor_help_response_time',
            field=models.CharField(choices=[('1H', '1 hour'), ('3H', '3 hours'), ('6H', '6 hours'), ('12H', '12 hours'), ('1D', '1 day'), ('2D', '2-3 days'), ('4D', '4-5 days'), ('6D', '6-7 days'), ('>7D', '> 7 days')], default='>7D', max_length=1, verbose_name='How long does it take for <b>your mentor</b> to respond to your requests for help?'),
        ),
        migrations.AddField(
            model_name='midpointinternfeedback',
            name='mentor_review_response_time',
            field=models.CharField(choices=[('1H', '1 hour'), ('3H', '3 hours'), ('6H', '6 hours'), ('12H', '12 hours'), ('1D', '1 day'), ('2D', '2-3 days'), ('4D', '4-5 days'), ('6D', '6-7 days'), ('>7D', '> 7 days')], default='>7D', max_length=3, verbose_name='How long does it take for <b>your mentor</b> to give feedback on your contributions?'),
        ),
        migrations.AddField(
            model_name='midpointmentorfeedback',
            name='mentor_help_response_time',
            field=models.CharField(choices=[('1H', '1 hour'), ('3H', '3 hours'), ('6H', '6 hours'), ('12H', '12 hours'), ('1D', '1 day'), ('2D', '2-3 days'), ('4D', '4-5 days'), ('6D', '6-7 days'), ('>7D', '> 7 days')], default='>7D', max_length=1, verbose_name="How long does it take for <b>you</b> to respond to your intern's request for help?"),
        ),
        migrations.AddField(
            model_name='midpointmentorfeedback',
            name='mentor_review_response_time',
            field=models.CharField(choices=[('1H', '1 hour'), ('3H', '3 hours'), ('6H', '6 hours'), ('12H', '12 hours'), ('1D', '1 day'), ('2D', '2-3 days'), ('4D', '4-5 days'), ('6D', '6-7 days'), ('>7D', '> 7 days')], default='>7D', max_length=3, verbose_name="How long does it take for <b>you</b> to give feedback on your intern's contributions?"),
        ),
        migrations.AlterField(
            model_name='midpointinternfeedback',
            name='intern_contribution_revision_time',
            field=models.CharField(choices=[('1H', '1 hour'), ('3H', '3 hours'), ('6H', '6 hours'), ('12H', '12 hours'), ('1D', '1 day'), ('2D', '2-3 days'), ('4D', '4-5 days'), ('6D', '6-7 days'), ('>7D', '> 7 days')], default='>7D', max_length=1, verbose_name="How long does it take for <b>you</b> to incorporate your mentor's feedback and resubmit a contribution?"),
        ),
        migrations.AlterField(
            model_name='midpointinternfeedback',
            name='intern_help_requests_frequency',
            field=models.CharField(choices=[('0', 'I have not asked for help'), ('D', 'Once per day'), ('M', 'Multiple times per week'), ('W', 'Once per week'), ('B', 'Every other week')], default='0', max_length=1, verbose_name="How often do <b>you</b> ask for your mentor's help?"),
        ),
        migrations.AlterField(
            model_name='midpointmentorfeedback',
            name='intern_contribution_revision_time',
            field=models.CharField(choices=[('1H', '1 hour'), ('3H', '3 hours'), ('6H', '6 hours'), ('12H', '12 hours'), ('1D', '1 day'), ('2D', '2-3 days'), ('4D', '4-5 days'), ('6D', '6-7 days'), ('>7D', '> 7 days')], default='>7D', max_length=1, verbose_name='How long does it take for <b>your intern</b> to incorporate feedback and resubmit a contribution?'),
        ),
        migrations.AlterField(
            model_name='midpointmentorfeedback',
            name='intern_help_requests_frequency',
            field=models.CharField(choices=[('0', 'Intern has not asked for help'), ('D', 'Once per day'), ('M', 'Multiple times per week'), ('W', 'Once per week'), ('B', 'Every other week')], default='0', max_length=1, verbose_name='How often does <b>your intern</b> ask for your help?'),
        ),
    ]