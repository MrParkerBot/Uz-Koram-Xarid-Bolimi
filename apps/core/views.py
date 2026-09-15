"""Views for the initial procurement service shell."""

from __future__ import annotations

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    """Render the initial application shell."""
    return render(request, "core/home.html")
