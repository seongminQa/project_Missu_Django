# Generated by Django 4.1.5 on 2023-02-06 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BugsWeekTop",
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
                ("rank", models.IntegerField(verbose_name="순위")),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="", verbose_name="앨범커버"
                    ),
                ),
                ("musician", models.CharField(max_length=200, verbose_name="가수")),
                ("title", models.CharField(max_length=200, verbose_name="곡명")),
                ("album", models.CharField(max_length=300, verbose_name="앨범명")),
                ("released_at", models.CharField(max_length=200, verbose_name="발매일")),
                ("genre", models.CharField(max_length=200, verbose_name="장르/스타일")),
                ("released_cop", models.CharField(max_length=150, verbose_name="발매사")),
                ("planned_cop", models.CharField(max_length=150, verbose_name="기획사")),
            ],
        ),
        migrations.CreateModel(
            name="GeniWeekTop",
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
                ("rank", models.IntegerField(verbose_name="순위")),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="", verbose_name="앨범커버"
                    ),
                ),
                ("title", models.CharField(max_length=200, verbose_name="곡명")),
                ("musician", models.CharField(max_length=150, verbose_name="가수")),
                ("album", models.CharField(max_length=300, verbose_name="앨범명")),
                ("released_at", models.CharField(max_length=200, verbose_name="발매일")),
                ("genre", models.CharField(max_length=200, verbose_name="장르/스타일")),
                ("released_cop", models.CharField(max_length=150, verbose_name="발매사")),
                ("planned_cop", models.CharField(max_length=150, verbose_name="기획사")),
            ],
        ),
        migrations.CreateModel(
            name="MelonWeekTop",
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
                ("rank", models.IntegerField(verbose_name="순위")),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="", verbose_name="앨범커버"
                    ),
                ),
                ("title", models.CharField(max_length=200, verbose_name="곡명")),
                ("musician", models.CharField(max_length=150, verbose_name="가수")),
                ("album", models.CharField(max_length=300, verbose_name="앨범명")),
                ("released_at", models.CharField(max_length=200, verbose_name="발매일")),
                ("genre", models.CharField(max_length=200, verbose_name="장르/스타일")),
                ("released_cop", models.CharField(max_length=150, verbose_name="발매사")),
                ("planned_cop", models.CharField(max_length=150, verbose_name="기획사")),
            ],
        ),
    ]
