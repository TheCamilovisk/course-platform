# Generated by Django 5.2 on 2025-06-13 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailverificationevent',
            name='last_attempt_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
