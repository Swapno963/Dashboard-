# Generated by Django 4.2.7 on 2024-07-18 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydashbord', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashbordmodel',
            name='published',
            field=models.CharField(max_length=150),
        ),
    ]
