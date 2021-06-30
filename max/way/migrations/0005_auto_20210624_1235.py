# Generated by Django 3.2.3 on 2021-06-24 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('way', '0004_auto_20210624_1215'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bot_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.IntegerField(default=0, null=True)),
                ('first_name', models.CharField(max_length=123, null=True)),
                ('last_name', models.CharField(max_length=125, null=True)),
                ('contact', models.CharField(max_length=120, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'bot_user',
            },
        ),
        migrations.DeleteModel(
            name='Bot_reg',
        ),
    ]
