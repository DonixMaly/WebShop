# Generated by Django 5.1.6 on 2025-02-26 12:26
 
from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = [
    ]
    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100)),
                ('opis', models.TextField()),
                ('cena', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]