# Generated by Django 2.2.9 on 2020-01-23 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('archivage', '0005_auto_20200123_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entreprise',
            name='development',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='archivage.Development'),
        ),
        migrations.AlterField(
            model_name='entreprise',
            name='formation',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='archivage.Formation'),
        ),
        migrations.AlterField(
            model_name='entreprise',
            name='marketing',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='archivage.Marketing'),
        ),
        migrations.AlterField(
            model_name='person',
            name='development',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='archivage.Development'),
        ),
        migrations.AlterField(
            model_name='person',
            name='formation',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='archivage.Formation'),
        ),
        migrations.AlterField(
            model_name='person',
            name='marketing',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='archivage.Marketing'),
        ),
    ]