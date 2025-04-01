from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    roll_number = models.CharField(max_length=20, unique=True)
    registration_number = models.CharField(max_length=20, unique=True)
    year_of_study = models.CharField(max_length=20)
    section = models.CharField(max_length=10)
    program = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    school = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.roll_number}"