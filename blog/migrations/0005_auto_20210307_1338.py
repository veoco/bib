# Generated by Django 3.1.7 on 2021-03-07 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210306_1317'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-order']},
        ),
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['-order', '-created']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-order', '-created']},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['-order']},
        ),
    ]
