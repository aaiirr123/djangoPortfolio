# Generated by Django 3.0.5 on 2020-05-04 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_lproject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computersciencep',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]