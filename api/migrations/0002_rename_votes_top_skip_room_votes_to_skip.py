# Generated by Django 3.2 on 2021-04-11 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='votes_top_skip',
            new_name='votes_to_skip',
        ),
    ]
