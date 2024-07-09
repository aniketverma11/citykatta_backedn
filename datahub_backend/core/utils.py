import os
from django.utils import timezone


def unique_filename(instance, filename):
    base, extension = os.path.splitext(filename)
    timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
    return f'documents/{base}_{timestamp}{extension}'
