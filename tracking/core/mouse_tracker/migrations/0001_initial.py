# Generated by Django 5.0.6 on 2024-06-25 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MouseEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('x_coordinate', models.IntegerField()),
                ('y_coordinate', models.IntegerField()),
                ('image_path', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
