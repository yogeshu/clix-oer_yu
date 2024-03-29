# Generated by Django 2.2 on 2019-06-02 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OxER', '0002_elibrary_oer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elibrary',
            name='oer',
        ),
        migrations.AlterField(
            model_name='elibrary',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='elibrary',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10000),
        ),
        migrations.AlterField(
            model_name='elibrary',
            name='summery',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='elibrary',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]
