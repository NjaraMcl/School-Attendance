# Generated by Django 4.0.5 on 2022-07-10 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainCore', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classe',
            old_name='teacher_id',
            new_name='teacher_responsable',
        ),
    ]