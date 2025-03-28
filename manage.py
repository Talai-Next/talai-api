#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Bus_Tracking.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

from django.core.management import execute_from_command_line
import os

if __name__ == "__main__":
    port = os.getenv('DJANGO_PORT', '8080')
    execute_from_command_line(['manage.py', 'runserver', f'127.0.0.1:{port}'])