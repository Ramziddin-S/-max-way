# Generated by Django 3.2.3 on 2021-06-24 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('way', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot_reg',
            name='contact',
            field=models.CharField(max_length=123, null=True),
        ),
        migrations.AlterField(
            model_name='bot_reg',
            name='first_name',
            field=models.CharField(max_length=123, null=True),
        ),
        migrations.AlterField(
            model_name='bot_reg',
            name='last_name',
            field=models.CharField(max_length=130, null=True),
        ),
    ]
