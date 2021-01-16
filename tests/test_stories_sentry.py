"""Tests related to stories_sentry module."""
from stories_sentry.exceptions import StorySentryError


def test_exception():
    """`StorySentryError` should be Exception subclass."""
    assert issubclass(StorySentryError, Exception)
