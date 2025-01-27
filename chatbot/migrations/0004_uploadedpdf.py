# Generated by Django 5.1.2 on 2024-11-06 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chatbot", "0003_remove_airesponse_confidence_score_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="UploadedPDF",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "pdf_file",
                    models.FileField(
                        upload_to="uploads/pdfs/", verbose_name="PDF File"
                    ),
                ),
                (
                    "uploaded_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Upload Time"),
                ),
            ],
        ),
    ]
