# Generated by Django 5.1.4 on 2024-12-12 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hodDashboard', '0002_registrarquotations_delete_purpose'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrarquotations',
            name='uploaded_pdf',
            field=models.FileField(upload_to='quotations/'),
        ),
    ]
