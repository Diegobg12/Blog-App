# Generated by Django 3.0.1 on 2020-07-22 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200721_0449'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='field_name',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='stars',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
