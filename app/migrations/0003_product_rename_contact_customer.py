# Generated by Django 4.2.2 on 2023-10-05 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_contact_phonenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=50)),
                ('quantity', models.IntegerField(max_length=100)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Contact',
            new_name='Customer',
        ),
    ]