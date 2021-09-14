from django.db import models


class Student(models.Model):
    rn = models.IntegerField()
    name = models.CharField(max_length=30)
    marks = models.FloatField()


class Laptop(models.Model):
    model_name=models.CharField(max_length=30)
    company=models.CharField(max_length=30)
    Ram=models.IntegerField()
    Rom=models.IntegerField()
    Weight=models.FloatField()
    Processor=models.CharField(max_length=30)


    def __str__(self):
        return  self.model_name