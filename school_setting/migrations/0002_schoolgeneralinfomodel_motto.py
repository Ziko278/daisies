# Generated by Django 4.2.1 on 2023-08-10 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_setting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolgeneralinfomodel',
            name='motto',
            field=models.CharField(default='the lord is my shepherd', max_length=250),
            preserve_default=False,
        ),
    ]