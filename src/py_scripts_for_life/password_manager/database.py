"""
SQLite Database module for Password Manager.

Handles all database operations:
- Creating and initializing the database
- Adding password entries
- Retrieving password entries
- Deleting password entries
- Resetting auto-increment when database is empty

Auto-increment behavior:
- IDs start at 1
- Continue progressively (1, 2, 3, 4...)
- When a single password is deleted (e.g., ID 2), next password gets ID 5 (continues from max)
- When ALL passwords are deleted, counter resets to 1
"""

import sqlite3
from pathlib import Path
from typing import List, Optional, Tuple


class PasswordDatabase:
    """
    Manages SQLite database for password storage.
    Each password entry has:
    - id: Unique identifier (auto-increment, resets to 1 when database empty)
    - website: Website/service name
    - email: Email address
    - encrypted_password: Encrypted password
    - created_at: Timestamp

    Auto-increment reset behavior:
    - Normally, IDs continue progressively (1, 2, 3, 4...)
    - Deleting a single password keeps the next ID progressive (if you delete ID 2, next is ID 5)
    - Deleting ALL passwords resets the counter to 1 for a fresh start
    """

    DB_PATH = "outputs/passwords.db"

    def __init__(self):
        """Initialize database connection and create table if needed."""
        Path("outputs").mkdir(exist_ok=True)
        self._create_table()

    def _create_table(self) -> None:
        """Create passwords table if it doesn't exist."""
        try:
            conn = sqlite3.connect(self.DB_PATH)
            cursor = conn.cursor()

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS passwords (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    website TEXT NOT NULL,
                    email TEXT NOT NULL,
                    encrypted_password TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )
                """
            )
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print(f"Database initialization error: {e}")

    def add_password(
        self, website: str, email: str, encrypted_password: str, created_at: str
    ) -> int:
        """
        Add a new password entry to the database.

        Args:
            website: Website/service name
            email: Email address
            encrypted_password: Encrypted password string
            created_at: Timestamp of creation

        Returns:
            The ID of the inserted password entry, or -1 on error
        """
        try:
            conn = sqlite3.connect(self.DB_PATH)
            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO passwords (website, email, encrypted_password, created_at)
                VALUES (?, ?, ?, ?)
                """,
                (website, email, encrypted_password, created_at),
            )

            password_id = cursor.lastrowid
            conn.commit()
            conn.close()

            return password_id
        except sqlite3.Error as e:
            print(f"Error adding password: {e}")
            return -1

    def get_all_passwords(self) -> List[Tuple]:
        """
        Retrieve all password entries from database.

        Returns:
            List of tuples (id, website, email, encrypted_password, created_at)
        """
        try:
            conn = sqlite3.connect(self.DB_PATH)
            cursor = conn.cursor()

            cursor.execute(
                "SELECT id, website, email, encrypted_password, created_at FROM passwords ORDER BY id DESC"
            )
            passwords = cursor.fetchall()
            conn.close()

            return passwords
        except sqlite3.Error as e:
            print(f"Error retrieving passwords: {e}")
            return []

    def get_password_by_id(self, password_id: int) -> Optional[Tuple]:
        """
        Retrieve a specific password entry by ID.

        Args:
            password_id: The ID of the password entry

        Returns:
            Tuple (id, website, email, encrypted_password, created_at) or None
        """
        try:
            conn = sqlite3.connect(self.DB_PATH)
            cursor = conn.cursor()

            cursor.execute(
                "SELECT id, website, email, encrypted_password, created_at FROM passwords WHERE id = ?",
                (password_id,),
            )
            password = cursor.fetchone()
            conn.close()

            return password
        except sqlite3.Error as e:
            print(f"Error retrieving password: {e}")
            return None

    def delete_password_by_id(self, password_id: int) -> bool:
        """
        Delete a password entry by ID.

        Does NOT reset auto-increment counter. Next password will continue from max ID.

        Args:
            password_id: The ID of the password entry to delete

        Returns:
            True if deletion was successful, False otherwise
        """
        try:
            conn = sqlite3.connect(self.DB_PATH)
            cursor = conn.cursor()

            cursor.execute("DELETE FROM passwords WHERE id = ?", (password_id,))
            conn.commit()
            rows_deleted = cursor.rowcount
            conn.close()

            return rows_deleted > 0
        except sqlite3.Error as e:
            print(f"Error deleting password: {e}")
            return False

    def delete_all_passwords(self) -> bool:
        """
        Delete all password entries from the database.
        ALSO resets the auto-increment counter back to 1 for a fresh start.

        Returns:
            True if deletion was successful, False otherwise
        """
        try:
            conn = sqlite3.connect(self.DB_PATH)
            cursor = conn.cursor()

            # Delete all passwords
            cursor.execute("DELETE FROM passwords")

            # Reset the auto-increment counter to 1 when database is completely empty
            # sqlite_sequence table tracks the next auto-increment value
            # Deleting the row resets the sequence, so next insert starts at 1
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='passwords'")

            conn.commit()
            conn.close()

            return True
        except sqlite3.Error as e:
            print(f"Error deleting all passwords: {e}")
            return False

    def get_password_count(self) -> int:
        """
        Get the total number of password entries.

        Returns:
            Number of passwords in database
        """
        try:
            conn = sqlite3.connect(self.DB_PATH)
            cursor = conn.cursor()

            cursor.execute("SELECT COUNT(*) FROM passwords")
            count = cursor.fetchone()[0]
            conn.close()

            return count
        except sqlite3.Error as e:
            print(f"Error getting password count: {e}")
            return 0
