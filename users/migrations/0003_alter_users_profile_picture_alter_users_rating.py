# Generated by Django 4.1.3 on 2022-11-10 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_users_is_premium_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='users',
            name='rating',
            field=models.FloatField(null=True),
        ),
    ]
