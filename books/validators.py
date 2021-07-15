from django.core.exceptions import ValidationError


def image_dimension_validator(image):
    if image.height != image.width:
        raise ValidationError('Image is not a square')
    return image
