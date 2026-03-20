# Password Manager

A secure command-line password manager with SQLite database storage, encryption support, and full CRUD operations.

## 🌟 Features

- **Generate Passwords**: Create secure random passwords with customizable length and character types (defaults to 18 characters)
- **Store Passwords**: Save passwords with website, email, and timestamp in SQLite database
- **Encryption**: All passwords encrypted using Fernet (industry-standard symmetric encryption)
- **Unique IDs**: Each password entry has an auto-incrementing ID for easy identification and management
- **View Passwords**: Retrieve and decrypt stored passwords with metadata
- **Delete Passwords**: Delete individual passwords by ID or clear entire database
- **Database Storage**: Structured SQLite database (`passwords.db`) instead of plain text files
- **Interactive CLI**: User-friendly command-line interface with abbreviations (a/v/d/q) for fast workflow and sensible defaults

## 🛠️ Tech Stack

- **Python** 3.10+ - Programming language
- **SQLite3** - Database engine (built-in)
- **Cryptography** - Fernet encryption library
- **Poetry** - Dependency management

## 📁 Project Structure

```
py_scripts_for_life/password_manager/
├── README.md                    # This file
├── app.py                       # Application CLI entry point
├── modes.py                     # Mode handlers (view, add, delete)
├── database.py                  # SQLite database operations
├── password_generator.py        # Password generation & encryption
└── __init__.py                  # Module initialization
```

## 📊 Database Structure

The SQLite database (`outputs/passwords.db`) contains a single `passwords` table:

```sql
CREATE TABLE passwords (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    website TEXT NOT NULL,
    email TEXT NOT NULL,
    encrypted_password TEXT NOT NULL,
    created_at TEXT NOT NULL
)
```

Each row represents one password entry with:
- **id**: Auto-incrementing unique identifier with smart reset behavior (see ID Management below)
- **website**: Website/service name (e.g., "gmail.com")
- **email**: Associated email address
- **encrypted_password**: Fernet-encrypted password
- **created_at**: Timestamp of creation

---

## 🆔 Smart ID Management

The password manager uses intelligent auto-increment ID management for a better user experience:

### Normal Usage (Adding Passwords)
IDs increment progressively starting from 1:
```
Add password 1 → ID: 1
Add password 2 → ID: 2
Add password 3 → ID: 3
Add password 4 → ID: 4
```

### Deleting Individual Passwords
When you delete a single password, the remaining passwords keep their IDs, and the next new password continues from the highest ID:

**Before deletion:**
```
ID: 1 (gmail.com)
ID: 2 (github.com)      ← Delete this one
ID: 3 (twitter.com)
ID: 4 (amazon.com)
```

**After deleting ID 2:**
```
ID: 1 (gmail.com)
ID: 3 (twitter.com)
ID: 4 (amazon.com)
```

**Next password added:**
```
ID: 1 (gmail.com)
ID: 3 (twitter.com)
ID: 4 (amazon.com)
ID: 5 (new_service.com) ← Continues from max ID (4)
```

### Deleting All Passwords (Delete All)
When you delete ALL passwords at once, the ID counter **resets to 1** for a fresh start:

**Before delete all:**
```
ID: 1 (gmail.com)
ID: 3 (twitter.com)
ID: 4 (amazon.com)
ID: 7 (linkedin.com)
```

**After "delete all" with confirmation:**
```
Database is empty
```

**Next password added after delete all:**
```
ID: 1 (new_gmail.com)   ← Resets to 1!
ID: 2 (new_github.com)  ← Continues normally
ID: 3 (new_twitter.com)
```

### Why This Behavior?

| Scenario | Behavior | Reason |
|----------|----------|--------|
| Delete single password | Keep other IDs, continue from max | Prevents ID gaps in normal usage |
| Delete all passwords | Reset to ID 1 | Fresh start, cleaner database state |
| Add after delete some | Continue progressive (5, 6, 7...) | Consistent, predictable numbering |
| Add after delete all | Start from 1 | Clean slate, intuitive restart |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Poetry
- Parent project dependencies installed

### Installation

From the project root:
```bash
poetry install
```

### Running the Password Manager

From the project root, start the application menu:
```bash
poetry run py-scripts-for-life
```

Then select option "1. Password Manager" from the menu.

Or run directly with:
```bash
poetry run python -m py_scripts_for_life.main
```

### First Time Setup

On first run, the application will:
1. Create `outputs/key.key` (encryption key)
2. Create `outputs/passwords.db` (SQLite database with passwords table)

⚠️ **Important**: Keep the `key.key` file safe! Without it, you cannot decrypt stored passwords.

---

## 💻 Usage

### Main Menu

When you start the Password Manager, you'll see:

```
Choose what mode do you want:
  (a)dd    - Add new password
  (v)iew   - View all passwords
  (d)elete - Delete password
  (q)uit   - Quit

Your choice: 
```

**You can use either abbreviations or full names:**
- `a` or `add` - Add new password
- `v` or `view` - View all passwords
- `d` or `delete` - Delete password
- `q` or `quit` - Exit application

### Adding a Password

1. Select **'a'** or **'add'** mode
2. Enter the website/service name (required - no default)
3. Enter your email address (required - no default)
4. Specify password length:
   - **Press Enter for default 18 characters**
   - Or enter a custom number
5. Choose whether to include digits (y/n)
6. Choose whether to include special characters (y/n)
7. Password is generated, encrypted, and saved automatically

**Example Output - Using Default:**
```
For what website will you use it? (q to quit): gmail.com
What email will you use it for? (q to quit): user@example.com

How many maximum characters in password do you want?
(press Enter for default 18, or q to quit): 

Using default password length: 18 characters

Do you want digits in your password? (y/n) (q to quit): y
Do you want special characters in your password? (y/n) (q to quit): y

✅ Password successfully saved with ID: 1
```

**Example Output - Custom Length:**
```
For what website will you use it? (q to quit): github.com
What email will you use it for? (q to quit): dev@example.com

How many maximum characters in password do you want?
(press Enter for default 18, or q to quit): 24

Do you want digits in your password? (y/n) (q to quit): y
Do you want special characters in your password? (y/n) (q to quit): y

✅ Password successfully saved with ID: 2
```

### Viewing Passwords

1. Select **'v'** or **'view'** mode
2. All stored passwords are displayed with:
   - **ID**: Unique identifier (used for deletion)
   - **Website**: Service name
   - **Email**: Associated email
   - **Password**: Decrypted password
   - **Created**: Timestamp

**Example Output:**
```
Total passwords: 2

ID: 2
Website: github.com
Email: dev@example.com
Password: aB9$xK2!mN@pQ7vR
Created: 03:45:22 Wed Mar-20-2024

ID: 1
Website: gmail.com
Email: user@example.com
Password: kL5&wM8*jP3#nO6!
Created: 02:30:15 Wed Mar-20-2024
```

### Deleting Passwords

#### Option 1: Delete by ID

1. Select **'d'** or **'delete'** mode
2. Choose **'id'** to delete a specific password
3. View available passwords with their IDs
4. Enter the ID of the password to delete
5. Confirm deletion (y/n)

**Example:**
```
Total passwords in database: 2

Delete by ID or delete all? (id/all) (q to quit): id

Available passwords:

  ID: 2 | Website: github.com | Email: dev@example.com
  ID: 1 | Website: gmail.com | Email: user@example.com

Enter the ID of the password to delete (q to quit): 1
Are you sure you want to delete ID 1 (gmail.com)? (y/n): y

✅ Password with ID 1 successfully deleted.
```

#### Option 2: Delete All

1. Select **'d'** or **'delete'** mode
2. Choose **'all'** to delete all passwords
3. **First confirmation**: "Are you sure you want to delete ALL passwords?"
4. **Second confirmation**: "This action CANNOT be undone. Are you absolutely sure?"
5. All passwords are deleted if you confirm both prompts

**Example:**
```
Total passwords in database: 2

Delete by ID or delete all? (id/all) (q to quit): all

⚠️  Are you sure you want to delete ALL passwords? (y/n): y
This action CANNOT be undone. Are you absolutely sure? (y/n): y

✅ All passwords successfully deleted.
```

---

## 🔐 Security Information

### Key File Management
- `key.key` contains the Fernet encryption key
- Automatically generated on first run in `outputs/` directory
- Required to decrypt all stored passwords
- **Never share** your key file
- **Never commit** to version control (excluded in .gitignore)
- Store in a secure location (consider backing up safely)

### Database Storage
- `passwords.db` is a standard SQLite database file
- **Passwords are encrypted** - the database file itself is not readable
- Without `key.key`, the encrypted passwords cannot be decrypted
- Database includes metadata: website, email, timestamp

### Encryption Details
- **Algorithm**: Fernet (symmetric encryption)
- **Standard**: HMAC + AES-128 in CBC mode
- **Python Library**: cryptography.fernet.Fernet
- **Strength**: Industry-standard, suitable for password storage
- **One-time Generation**: Each password encrypted immediately after generation

### Security Best Practices
- ✅ Passwords encrypted immediately after generation
- ✅ Key file excluded from version control
- ✅ No hardcoded secrets or credentials
- ✅ Proper SQLite error handling
- ✅ No plaintext password storage
- ✅ Double confirmation for "delete all" operation
- ❌ Do NOT lose key.key file
- ❌ Do NOT share key.key file
- ❌ Do NOT commit key.key to version control

---

## 📂 Data Flow

```
1. User Input (website, email, preferences)
   ↓
2. Password Generation (PasswordGenerator)
   ↓
3. Encryption (Fernet cipher)
   ↓
4. Database Storage (SQLite passwords.db with auto-increment ID)
   ↓
5. Retrieval & Decryption (View mode)
   ↓
6. Display to User with ID and metadata
```

---

## 🔧 Configuration

### Database Location
Default storage location: `outputs/passwords.db`

To customize storage location, modify `database.py`:
```python
DB_PATH = "outputs/passwords.db"  # Change this path
```

### Encryption Key Location
Default storage location: `outputs/key.key`

To customize, modify `password_generator.py`:
```python
with open("outputs/key.key", "rb") as key_file:
    # Change "outputs/key.key" to desired path
```

---

## 📊 Implementation Details

### PasswordDatabase Class
Core database operations:
```
Methods:
  - add_password() - Add new entry, returns ID
  - get_all_passwords() - Retrieve all entries
  - get_password_by_id() - Retrieve specific entry
  - delete_password_by_id() - Delete by ID
  - delete_all_passwords() - Clear entire database
  - get_password_count() - Get total entries
```

### PasswordGenerator Class
Password generation with encryption:
```
Attributes:
  - max_character: int (password length)
  - numbers: bool (include digits)
  - special_characters: bool (include special chars)

Methods:
  - encryptor() -> Fernet (load/create encryption key)
  - generator() -> str (generate encrypted password)
```

### PasswordManager Class
Combines generation with metadata:
```
Attributes:
  - website: str
  - email: str
  - password: str (encrypted)
  - time_now: str (creation timestamp)

Methods:
  - what_website() -> str
  - what_email() -> str
  - what_password() -> str
  - what_time() -> str
```

### PasswordMode Class
Handles all user interactions:
```
Methods:
  - view() - Display all passwords
  - add() - Add new password
  - delete() - Delete password(s)
  - _delete_by_id() - Delete specific ID
  - _delete_all() - Delete all with confirmation
```

---

## ⚠️ Known Limitations

- Single encryption key for all passwords
- No master password authentication
- No password search functionality (use view mode to find)
- No password update/edit features (delete and re-add)
- No password strength meter
- No backup/restore functionality
- SQLite database not encrypted at rest (only individual passwords)

---

## 🚀 Future Enhancements

- [ ] Master password authentication
- [ ] Password search and filtering by website/email
- [ ] Password update/edit functionality
- [ ] Password strength indicator
- [ ] Backup and restore functionality
- [ ] Password expiry notifications
- [ ] Multi-user support
- [ ] Database-level encryption
- [ ] GUI application (tkinter/PyQt)
- [ ] Cloud synchronization
- [ ] Password complexity rules

---

## 🤝 Contributing

When adding features:
1. Maintain the modular structure
2. Follow existing code patterns
3. Add comprehensive docstrings
4. Include security considerations
5. Update this README with new features
6. Add error handling
7. Test all modes (add, view, delete)

---

## 📝 License

See [LICENSE](../../../LICENSE) in the project root.

---

**Status**: ✅ Major Update - SQLite Database & Delete Mode
**Last Updated**: 2024