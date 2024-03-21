from django.core.exceptions import ValidationError
import re

def validate_name(str_name):
    error_message = 'Name must be in the format "First Middle Initial. Last"'

    name_pattern = r'^[A-Z][a-z]+ [A-Z]\. [A-Z][a-z]+$'

    good_name = re.match(name_pattern, str_name)

    if good_name:
        return str_name
    else:
        raise ValidationError(error_message, params={'name':str_name})
    
def validate_school_email(str_email):
    error_message = 'Invalid school email format. Please use an email ending with "@school.com".'

    email_pattern = r'^\w+\@school\.com$'

    good_email = re.match(email_pattern, str_email)

    if good_email:
        return str_email
    else:
        raise ValidationError(error_message, params={'student_email':str_email})
    
def validate_combination_format(str_combination):
    error_message = 'Combination must be in the format "12-12-12"'

    combination_pattern = r'^\d{2}-\d{2}-\d{2}$'

    good_combination = re.match(combination_pattern, str_combination)

    if good_combination:
        return str_combination
    else:
        raise ValidationError(error_message, params={'locker_combination':str_combination} )