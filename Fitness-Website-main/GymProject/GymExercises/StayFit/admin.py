from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(MuscleGroup)
admin.site.register(GExercise)
admin.site.register(HExercise)
admin.site.register(S_Exercise)
admin.site.register(Yoga)
admin.site.register(Product)
admin.site.register(Tag)
