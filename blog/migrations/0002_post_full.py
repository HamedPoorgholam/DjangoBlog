# Generated by Django 3.2.14 on 2022-08-11 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='full',
            field=models.TextField(null=True),
        ),
    ]
