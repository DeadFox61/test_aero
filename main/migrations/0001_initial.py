# Generated by Django 3.2.7 on 2021-09-30 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interface',
            fields=[
                ('ifindex', models.IntegerField(primary_key=True, serialize=False)),
                ('ifname', models.CharField(blank=True, max_length=256)),
                ('mtu', models.IntegerField()),
                ('operstate', models.CharField(blank=True, max_length=256)),
                ('mac_address', models.CharField(blank=True, max_length=256)),
                ('ip', models.GenericIPAddressField()),
            ],
        ),
    ]