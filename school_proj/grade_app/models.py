from django.db import models
from django.core import validators as v
from student_app.models import Student
from subject_app.models import Subject
# Create your models here.

class Grade(models.Model):
    grade = models.DecimalField(null=False, max_digits=5, decimal_places=2, default=100, validators=[v.MaxValueValidator(100.00), v.MinValueValidator(0.00)])
    a_subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)