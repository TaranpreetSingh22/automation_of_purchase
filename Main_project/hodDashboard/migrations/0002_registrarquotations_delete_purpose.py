# Generated by Django 5.1.4 on 2024-12-12 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hodDashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrarQuotations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=255)),
                ('item', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('uploaded_pdf', models.FileField(upload_to='registrar_quotations/')),
                ('status', models.CharField(choices=[('Pending', 'Pending Registrar Approval'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Purpose',
        ),
    ]