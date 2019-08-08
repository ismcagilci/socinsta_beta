# Generated by Django 2.1.7 on 2019-08-08 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_results', '0004_auto_20190516_0412'),
        ('aristo', '0009_remove_api_settings_main_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='django_celery_results.TaskResult')),
            ],
        ),
    ]