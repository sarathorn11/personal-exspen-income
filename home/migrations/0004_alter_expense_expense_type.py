# Generated by Django 4.2.1 on 2023-05-18 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_expense_amount_expense_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='expense_type',
            field=models.CharField(choices=[('Positive', 'Positive'), ('Negative', 'Negative')], max_length=100),
        ),
    ]
