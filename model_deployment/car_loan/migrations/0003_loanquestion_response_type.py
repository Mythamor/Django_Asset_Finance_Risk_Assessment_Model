# Generated by Django 5.1.2 on 2024-10-20 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("car_loan", "0002_borrowerresponse_response_text_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="loanquestion",
            name="response_type",
            field=models.CharField(
                choices=[("string", "String"), ("integer", "Integer")],
                default="integer",
                max_length=10,
            ),
        ),
    ]
