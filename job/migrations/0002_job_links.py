# Generated by Django 2.0.2 on 2020-04-04 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='links',
            field=models.CharField(default='SOME STRING', max_length=255),
        ),
    ]
