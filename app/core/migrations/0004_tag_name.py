# Generated by Django 3.0.8 on 2020-07-11 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]