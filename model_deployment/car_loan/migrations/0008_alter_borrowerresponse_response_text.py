# Generated by Django 5.1.2 on 2024-10-22 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("car_loan", "0007_alter_borrowerresponse_selected_option"),
    ]

    operations = [
        migrations.AlterField(
            model_name="borrowerresponse",
            name="response_text",
            field=models.PositiveBigIntegerField(null=True),
        ),
    ]
