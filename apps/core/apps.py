"""Core application configuration."""

from __future__ import annotations

from django.apps import AppConfig


class CoreConfig(AppConfig):
    """Configure shared foundation behavior for the core app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.core"
    verbose_name = "Core"
