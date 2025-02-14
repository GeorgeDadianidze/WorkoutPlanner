# Generated by Django 5.1.5 on 2025-02-04 10:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("workouts", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ExerciseAchievement",
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
                    "max_weight",
                    models.FloatField(
                        blank=True,
                        help_text="Max weight lifted (if applicable)",
                        null=True,
                    ),
                ),
                (
                    "max_reps",
                    models.IntegerField(
                        blank=True, help_text="Max reps achieved", null=True
                    ),
                ),
                (
                    "best_time",
                    models.FloatField(
                        blank=True,
                        help_text="Best time in seconds (if applicable)",
                        null=True,
                    ),
                ),
                ("date_achieved", models.DateField(auto_now_add=True)),
                (
                    "exercise",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="workouts.exercise",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="exercise_achievements",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FitnessGoal",
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
                    "goal_type",
                    models.CharField(
                        choices=[
                            ("weight_loss", "Weight Loss"),
                            ("muscle_gain", "Muscle Gain"),
                            ("endurance", "Endurance"),
                            ("strength", "Strength"),
                            ("general_fitness", "General Fitness"),
                        ],
                        default="general_fitness",
                        max_length=20,
                    ),
                ),
                (
                    "target_weight",
                    models.FloatField(
                        blank=True,
                        help_text="Target weight in kg (if applicable)",
                        null=True,
                    ),
                ),
                (
                    "target_date",
                    models.DateField(help_text="Deadline for achieving the goal"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="fitness_goals",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="WeightTracking",
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
                ("weight", models.FloatField(help_text="User weight in kg")),
                ("date", models.DateField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="weight_entries",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
