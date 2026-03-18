"""
Shared utilities module for py-scripts-for-life.

Exports common UI graphics and formatting functions used across all scripts.
"""

from .graphics import closing, data_border, main_title, read_border, script_title

__all__ = [
    "main_title",
    "closing",
    "read_border",
    "data_border",
    "script_title",
]
