# Generated by Django 2.2.6 on 2019-10-21 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-id',)},
        ),
    ]