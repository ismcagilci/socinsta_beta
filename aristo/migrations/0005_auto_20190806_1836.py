# Generated by Django 2.1.7 on 2019-08-06 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aristo', '0004_auto_20190806_1834'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assistants_settings',
            old_name='is_bussines',
            new_name='is_busines',
        ),
    ]
