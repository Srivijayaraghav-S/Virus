# Generated by Django 4.1.2 on 2022-10-15 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_remove_students_roll'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Students',
        ),
    ]