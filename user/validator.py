from django.core.exceptions import ValidationError

def password_validate(password):
    if len(password) < 8:
        raise ValidationError(("Too short password"), code = 'invalid')