# Generated by Django 4.1.3 on 2022-11-07 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=50)),
                ('post_restaurant', models.CharField(max_length=30)),
                ('post_content', models.TextField()),
                ('post_image', models.ImageField(blank=True, upload_to='$Y/%m')),
                ('post_created', models.DateTimeField(auto_now_add=True)),
                ('post_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.TextField()),
                ('comment_created', models.DateTimeField(auto_now_add=True)),
                ('comment_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'comment',
            },
        ),
    ]
