from django.db import models
from django.urls import reverse


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    about = models.CharField(max_length=1024)

    def __str__(self):
        return f'{self.name} {self.surname}'

    def get_detail_url(self):
        return reverse('teacher-detail', args=(self.pk,))


class Course(models.Model):
    title = models.CharField(max_length=255)
    info = models.CharField(max_length=1024)
    duration_months = models.IntegerField()
    price = models.FloatField()
    teacher = models.ManyToManyField(Teacher)

    def __str__(self):
        return self.title

    def get_detail_url(self):
        return reverse('course-detail', args=(self.pk,))


class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    course = models.ManyToManyField(Course)

    def __str__(self):
        return f'{self.name} {self.surname}'
