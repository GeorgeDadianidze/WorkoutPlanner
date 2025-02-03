from django.contrib.auth.models import User
from django.db import models


class Exercise(models.Model):
    """Predefined exercise with details."""

    name = models.CharField(max_length=255)
    description = models.TextField()
    target_muscles = models.CharField(max_length=255)
    instructions = models.TextField()

    def __str__(self):
        return self.name


class WorkoutPlan(models.Model):
    """User's personalized workout plan."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    goal = models.TextField()
    frequency_per_week = models.IntegerField()
    session_duration = models.IntegerField(help_text="Duration in minutes")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.user.username}"


class WorkoutExercise(models.Model):
    """Exercises linked to a user's workout plan."""

    workout_plan = models.ForeignKey(
        WorkoutPlan, on_delete=models.CASCADE, related_name="exercises"
    )
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.IntegerField()
    repetitions = models.IntegerField(null=True, blank=True)
    duration = models.IntegerField(
        null=True, blank=True, help_text="Duration in seconds"
    )
    distance = models.FloatField(null=True, blank=True, help_text="Distance in km")

    def __str__(self):
        return f"{self.exercise.name} in {self.workout_plan.name}"
