# Generated by Django 4.2.7 on 2023-12-25 16:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('fileshare', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='file',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='file')),
                ('create_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='folder',
            name='name',
        ),
        migrations.AddField(
            model_name='folder',
            name='create_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='folder',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
