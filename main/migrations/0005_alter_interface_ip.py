# Generated by Django 3.2.7 on 2021-09-30 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_interface_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interface',
            name='ip',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]