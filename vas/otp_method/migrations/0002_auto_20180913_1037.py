# Generated by Django 2.0.7 on 2018-09-13 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('otp_method', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='otp',
            old_name='recipient',
            new_name='receipient',
        ),
    ]