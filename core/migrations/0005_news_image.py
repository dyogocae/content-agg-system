# Generated by Django 3.2.9 on 2021-11-08 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_news_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
