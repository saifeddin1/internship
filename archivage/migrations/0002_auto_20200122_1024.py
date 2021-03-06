# Generated by Django 2.2.9 on 2020-01-22 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('archivage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entreprise',
            name='development',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='archivage.Development'),
        ),
        migrations.AlterField(
            model_name='entreprise',
            name='formation',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='archivage.Formation'),
        ),
        migrations.AlterField(
            model_name='entreprise',
            name='marketing',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='archivage.Marketing'),
        ),
        migrations.AlterField(
            model_name='person',
            name='development',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='archivage.Development'),
        ),
        migrations.AlterField(
            model_name='person',
            name='formation',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='archivage.Formation'),
        ),
        migrations.AlterField(
            model_name='person',
            name='marketing',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='archivage.Marketing'),
        ),
    ]
