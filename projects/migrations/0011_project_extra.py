# Generated by Django 2.1.1 on 2020-05-14 22:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20200506_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='extra',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]