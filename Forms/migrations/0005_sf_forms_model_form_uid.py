# Generated by Django 3.2.7 on 2021-09-17 13:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Forms', '0004_auto_20210917_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='sf_forms_model',
            name='Form_UID',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
