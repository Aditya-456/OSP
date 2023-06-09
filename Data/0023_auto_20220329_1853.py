# Generated by Django 2.2.5 on 2022-03-29 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_auto_20220329_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Out for delivery', 'Out for delivery'), ('Pending', 'Pending'), ('Delivered', 'Delivered')], max_length=200, null=True),
        ),
    ]
