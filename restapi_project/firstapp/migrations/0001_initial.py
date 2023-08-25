# Generated by Django 4.2.4 on 2023-08-25 10:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="cert_category_master",
            fields=[
                (
                    "cat_id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("cat_name", models.CharField(blank=True, max_length=50, null=True)),
                ("createdby", models.CharField(max_length=40)),
                ("timestamp", models.DateTimeField(default=datetime.datetime.now)),
                ("delete1", models.IntegerField(default=0)),
            ],
            options={
                "db_table": "cert_category_master",
            },
        ),
        migrations.CreateModel(
            name="emp_skill_cert_master",
            fields=[
                (
                    "cid",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("cat", models.IntegerField()),
                ("cert_name", models.CharField(max_length=50)),
                ("tcode_substr", models.CharField(max_length=10, null=True)),
                ("createdby", models.CharField(max_length=40)),
                ("timestamp", models.DateTimeField(default=datetime.datetime.now)),
                ("delete1", models.IntegerField(default=0)),
            ],
            options={
                "db_table": "emp_skill_cert_master",
            },
        ),
        migrations.CreateModel(
            name="expert_employee",
            fields=[
                (
                    "exp_id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("cid", models.IntegerField()),
                ("expert_empcode", models.IntegerField()),
                ("sub_cat", models.IntegerField()),
                ("createdby", models.CharField(blank=True, max_length=10, null=True)),
                ("delete1", models.IntegerField(default=0)),
                ("timestamp", models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                "db_table": "expert_employee",
            },
        ),
        migrations.CreateModel(
            name="skill_field_master",
            fields=[
                (
                    "field_id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("cert_id", models.IntegerField(blank=True, null=True)),
                ("skill", models.IntegerField(blank=True, null=True)),
                ("field_value", models.CharField(blank=True, max_length=50, null=True)),
                ("seq", models.IntegerField()),
                ("createdby", models.CharField(blank=True, max_length=10, null=True)),
                ("delete1", models.IntegerField(default=0)),
                (
                    "timestamp",
                    models.DateField(
                        verbose_name=datetime.datetime(
                            2023,
                            8,
                            25,
                            10,
                            26,
                            59,
                            683162,
                            tzinfo=datetime.timezone.utc,
                        )
                    ),
                ),
            ],
            options={
                "db_table": "skill_field_master",
            },
        ),
        migrations.CreateModel(
            name="skill_field_master_inputs",
            fields=[
                (
                    "field_id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("cert_id", models.IntegerField(blank=True, null=True)),
                ("skill", models.IntegerField(blank=True, null=True)),
                ("field_value", models.CharField(blank=True, max_length=50, null=True)),
                ("input", models.CharField(blank=True, max_length=500, null=True)),
                ("seq", models.IntegerField()),
                ("createdby", models.CharField(blank=True, max_length=10, null=True)),
                ("delete1", models.IntegerField(default=0)),
                (
                    "timestamp",
                    models.DateField(
                        verbose_name=datetime.datetime(
                            2023,
                            8,
                            25,
                            10,
                            26,
                            59,
                            683611,
                            tzinfo=datetime.timezone.utc,
                        )
                    ),
                ),
            ],
            options={
                "db_table": "skill_field_masterV1",
            },
        ),
        migrations.CreateModel(
            name="skill_fields",
            fields=[
                (
                    "skill_id",
                    models.IntegerField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("field_name", models.CharField(default=0, max_length=50)),
                ("createdby", models.CharField(blank=True, max_length=10, null=True)),
                ("delete1", models.IntegerField(default=0)),
                ("timestamp", models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                "db_table": "skill_fields",
            },
        ),
    ]