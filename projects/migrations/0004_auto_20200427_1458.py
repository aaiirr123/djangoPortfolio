# Generated by Django 3.0.5 on 2020-04-27 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20200427_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='learn',
            field=models.TextField(default='aaron'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='secondaryImages',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
