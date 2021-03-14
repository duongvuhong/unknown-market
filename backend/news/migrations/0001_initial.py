# Generated by Django 3.1.6 on 2021-03-14 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('thumbnail', models.URLField()),
            ],
        ),
    ]
