# Generated by Django 3.2.7 on 2021-09-25 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Forms', '0009_sf_cloudinary_bin_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='sf_options_model',
            name='Question_Id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Forms.sf_question_model'),
            preserve_default=False,
        ),
    ]
