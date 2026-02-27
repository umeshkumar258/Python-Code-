#!/usr/bin/env python3
"""
Django's command-line utility for administrative tasks.
Improved version with better structure and error handling.
"""

import os
import sys


def main() -> None:
    """
    Run administrative tasks for the Django project.
    """
    settings_module = "mywebsite.settings"
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as error:
        print("\n❌ Django is not installed or not available in your environment.")
        print("👉 Possible reasons:")
        print("   - Virtual environment not activated")
        print("   - Django not installed (pip install django)")
        print("   - Wrong PYTHONPATH configuration\n")
        raise error

    try:
        execute_from_command_line(sys.argv)
    except Exception as error:
        print(f"\n⚠️ An error occurred while running the command: {error}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
