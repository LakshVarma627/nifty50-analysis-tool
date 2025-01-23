#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
        execute_from_command_line(sys.argv)
    except ImportError as exc:
        raise ImportError("Couldn't import Django. Are you in a virtual environment?") from exc
    except Exception as e:
        import logging
        logging.basicConfig(level=logging.ERROR)
        logging.error("An error occurred during migration: %s", e)
        sys.exit(1)

if __name__ == '__main__':
    main()
