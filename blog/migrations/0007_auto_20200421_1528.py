# Generated by Django 2.1.15 on 2020-04-21 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='photo',
            field=models.ImageField(upload_to='photos'),
        ),
    ]
