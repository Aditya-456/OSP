# Generated by Django 2.2.5 on 2022-03-28 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20220328_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Out for delivery', 'Out for delivery'), ('Pending', 'Pending')], max_length=200, null=True),
        ),
    ]
