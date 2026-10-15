"""Alchemy package initialization.

Exposes create_air directly on the package interface, leaving create_earth hidden.
"""

from .elements import create_air

__all__ = ["create_air"]
