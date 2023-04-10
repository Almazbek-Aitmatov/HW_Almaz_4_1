# Generated by Django 4.2 on 2023-04-10 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='app',
            new_name='age',
        ),
        migrations.AlterField(
            model_name='purchase',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='shop.item'),
        ),
    ]
