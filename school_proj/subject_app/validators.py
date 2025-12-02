from django.core.exceptions import ValidationError
import re


def validate_subject_name(name):
    name_pattern = re.compile(r'^[A-Z][a-z]+(?:\s[A-Z][a-z]+)*$')
    
    if not name_pattern.match(name):
        raise ValidationError("Subject must be in title case format.")


def validate_professor_name(name):
    name_pattern = re.compile(r'^Professor\s[A-Z][a-z]+(?:\s[A-Z][a-z]+)*$')
    
    if not name_pattern.match(name):
        raise ValidationError(
            'Professor name must be in the format "Professor Adam".'
        )