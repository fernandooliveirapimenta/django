# Generated by Django 3.0.2 on 2020-01-11 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_post_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='subtitle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
