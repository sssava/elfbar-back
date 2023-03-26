# Generated by Django 4.1 on 2023-03-26 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elfbar_api', '0013_alter_orderitem_elfbar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='elfbar',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='elfbar', to='elfbar_api.elfbar'),
            preserve_default=False,
        ),
    ]