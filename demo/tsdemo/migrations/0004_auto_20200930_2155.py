# Generated by Django 3.0.5 on 2020-09-30 13:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tsdemo', '0003_testpro'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testpro',
            old_name='ispass',
            new_name='isPass',
        ),
        migrations.AddField(
            model_name='testpro',
            name='tsdate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
