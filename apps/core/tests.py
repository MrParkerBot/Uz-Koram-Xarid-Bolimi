"""Smoke tests for the initial Django foundation."""

from __future__ import annotations

from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):
    """Verify that the initial browser route is wired correctly."""

    def test_home_page_renders_project_shell(self) -> None:
        response = self.client.get(reverse("core:home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Uz-Koram Xarid Xizmati")
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "core/home.html")
