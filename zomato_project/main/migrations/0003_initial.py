# Generated by Django 4.2.3 on 2023-07-27 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0002_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images')),
                ('status', models.BooleanField(default=False, help_text='0=default,1=Hidden')),
            ],
        ),
    ]
