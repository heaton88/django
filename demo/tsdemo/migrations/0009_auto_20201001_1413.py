# Generated by Django 3.0.5 on 2020-10-01 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tsdemo', '0008_auto_20201001_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testpro',
            name='tsppro',
            field=models.CharField(max_length=10, verbose_name='所属产品'),
        ),
    ]