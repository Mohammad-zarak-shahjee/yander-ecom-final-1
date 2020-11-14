# Generated by Django 3.0.8 on 2020-10-16 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200925_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Shawls'), ('G', 'Gowns'), ('K', 'Kaftans'), ('SC', 'Scarfs'), ('D', 'Decor'), ('SF', 'Saffron'), ('H', 'Honey'), ('T', 'Tea'), ('DF', 'Dry-Fruits')], max_length=2),
        ),
        migrations.AlterField(
            model_name='order',
            name='ref_code',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
    ]
