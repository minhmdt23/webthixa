# Generated by Django 3.2.13 on 2022-06-02 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('man', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='conference',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='element',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='nameplate',
            options={'ordering': ['-id']},
        ),
    ]
