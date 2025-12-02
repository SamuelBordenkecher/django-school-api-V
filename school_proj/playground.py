from subject_app import validators
from subject_app import models

from django.db import models
from django.core import validators as v
from subject_app.models import Subject
from subject_app.validators import (
    validate_subject_name,
    validate_professor_name,
)


# Create your models here.

class Subject(models.Model):
    subject_name = models.CharField(null=False, unique=True, validators=[validate_subject_name])
    professor = models.CharField(null=False, default='Mr. Cahan', validators=[validate_professor_name])

    def __str__(self):
        return f"{self.subject_name} - {self.professor} - {self.students.count}"
    
    def add_a_student(self, id):
        count = self.students.count
        if count < 31:
            self.students.add(id)
        else:
            raise Exception("This subject is full!")
        
    def drop_a_student(self, id):
        if id in self.students and len(self.students) > 2:
            self.students.remove(id)
        else:
            raise Exception("This subject is empty!")
        

math = Subject(subject_name='Math', professor='Professor Chad')