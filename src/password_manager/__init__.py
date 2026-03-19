"""
Password Manager module for py-scripts-for-life.

A secure command-line password manager with encryption support.
Provides password generation, storage, and retrieval with Fernet encryption.

Main components:
- PasswordGenerator: Creates secure random passwords
- PasswordManager: Manages password storage and metadata
- PasswordMode: Handles user interaction (view/add modes)
"""

from .app import app

__all__ = ["app"]
