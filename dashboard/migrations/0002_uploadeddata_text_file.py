# Generated by Django 5.0.3 on 2024-03-22 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadeddata',
            name='text_file',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
