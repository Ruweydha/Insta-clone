# Generated by Django 4.0.2 on 2022-03-08 00:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_profile_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', tinymce.models.HTMLField()),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('commentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insta.images')),
            ],
        ),
    ]