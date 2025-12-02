from django.db import models
from django.core import validators as v
from .validators import (
    validate_subject_name,
    validate_professor_name,
)


# Create your models here.

class Subject(models.Model):
    subject_name = models.CharField(null=False, unique=True, validators=[validate_subject_name])
    professor = models.CharField(null=False, default='Mr. Cahan', validators=[validate_professor_name])

    def __str__(self):
        return f"{self.subject_name} - {self.professor}"
    
    @property
    def student_count(self):
        return self.students.count()
    
    def add_a_student(self, id):
        count = self.students.count()
        if count < 31:
            self.students.add(id)
        else:
            raise Exception("This subject is full!")
        
    def drop_a_student(self, student):
        if self.students.count() <= 2:
            raise Exception("This subject is empty!")

        if self.students.filter(pk=student.pk).exists():
            self.students.remove(student)
        else:
            raise Exception("Student is not enrolled in this subject.")

        

