from django.db import models


class StudentDetail(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField()
    standard = models.CharField(max_length=255)
    english = models.FloatField(default=0)
    physics = models.FloatField(default=0)
    maths = models.FloatField(default=0)
    chemistry = models.FloatField(default=0)
    biology = models.FloatField(default=0)
    history = models.FloatField(default=0)
    geography = models.FloatField(default=0)
