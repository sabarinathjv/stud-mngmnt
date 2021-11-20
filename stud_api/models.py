from django.db import models




class Mark(models.Model):
    name = models.CharField(max_length=255)
    marks = models.FloatField(default=0)


class StudentDetail(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField()
    standard = models.CharField(max_length=255)
    marks = models.ManyToManyField(Mark)



