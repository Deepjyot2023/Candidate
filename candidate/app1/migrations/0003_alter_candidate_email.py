# Generated by Django 3.2 on 2023-06-08 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_candidate_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='email',
            field=models.EmailField(blank=True, max_length=50, unique=True),
        ),
    ]
