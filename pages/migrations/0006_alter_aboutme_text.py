# Generated by Django 4.2.5 on 2023-10-02 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_alter_aboutme_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
