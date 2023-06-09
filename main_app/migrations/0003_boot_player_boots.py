# Generated by Django 4.2 on 2023-05-07 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_training'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('manufacturer', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='boots',
            field=models.ManyToManyField(to='main_app.boot'),
        ),
    ]
