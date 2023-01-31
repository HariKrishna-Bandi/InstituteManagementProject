from django.db import models

# Create your models here.
class city(models.Model):
    City_Name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.City_Name}'

class Course(models.Model):
    Course_Name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.Course_Name}'

class Student(models.Model):
    stud_Name = models.CharField(max_length=50)
    stud_Age = models.IntegerField()
    stud_phno = models.BigIntegerField()
    stud_City = models.ForeignKey(city,on_delete=models.CASCADE)
    stud_Course = models.ForeignKey(Course,on_delete=models.CASCADE)