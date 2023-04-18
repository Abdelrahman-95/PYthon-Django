# Generated by Django 4.2 on 2023-04-18 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Content', models.TextField(max_length=5000)),
                ('Image', models.ImageField(upload_to='posts/')),
            ],
        ),
    ]
