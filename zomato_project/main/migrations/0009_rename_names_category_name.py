# Generated by Django 4.2.3 on 2023-08-09 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_name_category_names'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='names',
            new_name='name',
        ),
    ]