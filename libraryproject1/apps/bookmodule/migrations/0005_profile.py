# Generated by Django 5.1.6 on 2025-05-04 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmodule', '0004_address22_student22'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='profile_photos/')),
            ],
        ),
    ]
