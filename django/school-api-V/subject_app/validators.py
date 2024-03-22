from django.core.exceptions import ValidationError
import re

def validate_subject_format(str_subject):
    error_message = 'Subject must be in title case format.'

    subject_pattern = r'^[A-Z][a-z]+(?: [A-Z][a-z]+)*$'

    good_subject = re.match(subject_pattern, str_subject)

    if good_subject:
        return str_subject
    else:
        raise ValidationError(error_message, params={'subject':str_subject})
    
def validate_professor_name(str_name):
    error_message = 'Professor name must be in the format "Professor Adam".'

    name_pattern = r'^Professor [A-Z][a-z]+$'

    good_name = re.match(name_pattern, str_name)

    if good_name:
        return str_name
    else:
        raise ValidationError(error_message, params={'professor':str_name})