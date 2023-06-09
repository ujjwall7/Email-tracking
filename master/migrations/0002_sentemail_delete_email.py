# Generated by Django 4.1.5 on 2023-05-26 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SentEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('to_email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('is_opened', models.BooleanField(default=False)),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Email',
        ),
    ]
