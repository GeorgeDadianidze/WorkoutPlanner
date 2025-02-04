from django.contrib import admin

from trackers.models import ExerciseAchievement, FitnessGoal, WeightTracking

# Register your models here.

admin.site.register(WeightTracking)
admin.site.register(FitnessGoal)
admin.site.register(ExerciseAchievement)
