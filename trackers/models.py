from django.contrib.auth.models import User
from django.db import models

from workouts.models import Exercise


class WeightTracking(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="weight_entries"
    )
    weight = models.FloatField(help_text="User weight in kg")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.weight} kg on {self.date}"


class FitnessGoal(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="fitness_goals"
    )
    goal_type = models.CharField(
        max_length=20,
        choices=[
            ("weight_loss", "Weight Loss"),
            ("muscle_gain", "Muscle Gain"),
            ("endurance", "Endurance"),
            ("strength", "Strength"),
            ("general_fitness", "General Fitness"),
        ],
        default="general_fitness",
    )
    target_weight = models.FloatField(
        null=True, blank=True, help_text="Target weight in kg (if applicable)"
    )
    target_date = models.DateField(help_text="Deadline for achieving the goal")

    def __str__(self):
        return f"{self.user.username} - {self.goal_type} goal by {self.target_date}"


class ExerciseAchievement(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="exercise_achievements"
    )
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    max_weight = models.FloatField(
        null=True, blank=True, help_text="Max weight lifted (if applicable)"
    )
    max_reps = models.IntegerField(null=True, blank=True, help_text="Max reps achieved")
    best_time = models.FloatField(
        null=True, blank=True, help_text="Best time in seconds (if applicable)"
    )
    date_achieved = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.exercise.name} achievement on {self.date_achieved}"
