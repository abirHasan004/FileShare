# Generated by Django 4.2.7 on 2023-12-25 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fileshare', '0003_alter_file_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='folder',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fileshare.folder'),
        ),
    ]
