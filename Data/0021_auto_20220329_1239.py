# Generated by Django 2.2.5 on 2022-03-29 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20220329_0554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], max_length=200, null=True),
        ),
    ]
