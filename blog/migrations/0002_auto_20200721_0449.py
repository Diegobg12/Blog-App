# Generated by Django 3.0.1 on 2020-07-21 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(null=True),
        ),
    ]
