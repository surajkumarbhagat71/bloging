# Generated by Django 2.2.7 on 2021-02-23 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blogview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogview',
            name='view',
            field=models.IntegerField(default=0),
        ),
    ]
