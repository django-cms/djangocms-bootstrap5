"""Pytest configuration for djangocms-bootstrap5 tests."""
import os
import django
from django.conf import settings


def pytest_configure():
    """Configure Django settings for pytest."""
    if not settings.configured:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tests.test_settings')
        django.setup()
