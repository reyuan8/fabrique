# Generated by Django 2.2.10 on 2021-05-05 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
