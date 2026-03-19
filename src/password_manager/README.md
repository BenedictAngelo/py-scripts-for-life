# Password Manager

A secure command-line password manager with encryption support using Fernet symmetric encryption.

## 🌟 Features

- **Generate Passwords**: Create secure random passwords with customizable length and character types
- **Store Passwords**: Save passwords with associated website and email information
- **Encryption**: All passwords encrypted using Fernet (industry-standard symmetric encryption)
- **View Passwords**: Retrieve and decrypt stored passwords with metadata
- **Interactive CLI**: User-friendly command-line interface with clear prompts
- **File-Based Storage**: Passwords stored in pipe-delimited format (website|email|password|timestamp)

## 🛠️ Tech Stack

- **Python** 3.10+ - Programming language
- **Cryptography** - Fernet encryption library
- **Poetry** - Dependency management

## 📁 Project Structure

```
password_manager/
├── README.md                    # This file
├── password_generator.py        # Core implementation
├── __init__.py                 # Module initialization
├── outputs/
│   ├── key.key                 # Encryption key (auto-generated)
│   └── passwords.txt           # Encrypted password storage
```

## 📋 Components Overview

### PasswordGenerator
Generates secure random passwords based on specified criteria:
- Customizable password length (minimum characters)
- Optional digit inclusion (0-9)
- Optional special character inclusion (!@#$%^&*)
- Automatic encryption of generated passwords
- Static `encryptor()` method for Fernet cipher management

### PasswordManager
Manages password storage with metadata:
- Stores website, email, encrypted password, and creation timestamp
- Inherits password generation from PasswordGenerator
- Provides getter methods for all stored data
- Integrates with file storage

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

From the project root:
```bash
poetry run python src/main.py
```

Then select option "1. Password Manager" from the menu.

### First Time Setup

On first run, the application will:
1. Create `outputs/key.key` (encryption key)
2. Create `outputs/passwords.txt` (encrypted password storage)

⚠️ **Important**: Keep the `key.key` file safe! Without it, you cannot decrypt stored passwords.

---

## 💻 Usage

### Adding a Password

1. Select "add" mode from the menu
2. Enter the website/service name
3. Enter your email address
4. Specify password length (digits only)
5. Choose whether to include digits (y/n)
6. Choose whether to include special characters (y/n)
7. Password is generated, encrypted, and saved automatically

### Viewing Passwords

1. Select "view" mode from the menu
2. All stored passwords are displayed with:
   - Website/Service name
   - Email address
   - Decrypted password
   - Creation timestamp

---

## 🔐 Security Information

### Key File Management
- `key.key` contains the encryption key (Fernet symmetric key)
- Automatically generated on first run
- Required to decrypt all stored passwords
- **Never share** your key file
- **Never commit** to version control (excluded in .gitignore)
- Store in a secure location (consider backing up safely)

### Password Storage Format
Passwords are stored in `outputs/passwords.txt` as pipe-delimited records:
```
website|email|encrypted_password|timestamp
```

Example:
```
google.com|user@example.com|gAAAAABl4XVz...|03:45:22 Mon Mar-18-2024
```

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
- ✅ Proper resource cleanup with context managers
- ✅ No plaintext password storage
- ❌ Do NOT lose key.key file
- ❌ Do NOT share key.key file
- ❌ Do NOT commit key.key to version control

---

## 📂 Data Flow

```
1. User Input
   ↓
2. Password Generation (PasswordGenerator)
   ↓
3. Encryption (Fernet cipher)
   ↓
4. File Storage (passwords.txt)
   ↓
5. Retrieval & Decryption (View mode)
   ↓
6. Display to User
```

---

## 🔧 Configuration

### Environment
Currently uses relative path `outputs/` for key and password storage.

To customize storage location, modify in `password_generator.py`:
```python
with open("outputs/key.key", "rb") as key_file:
    # Change "outputs/key.key" to desired path
```

---

## 📊 Implementation Details

### PasswordGenerator Class
```
Attributes:
  - max_character: int (minimum password length)
  - numbers: bool (include digits)
  - special_characters: bool (include special chars)

Methods:
  - __init__() - Initialize with options
  - encryptor() -> Fernet - Load/create encryption key
  - generator() -> str - Generate encrypted password
```

### PasswordManager Class
Extends PasswordGenerator with:
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

---

## ⚠️ Known Limitations

- File-based storage only (no database)
- No password search functionality
- No password update/delete features
- No password strength meter
- No master password authentication
- Single encryption key for all passwords
- No backup/restore functionality

---

## 🚀 Future Enhancements

- [ ] Migrate to SQLite database
- [ ] Add password search and filtering
- [ ] Implement password update/delete
- [ ] Add password strength indicator
- [ ] Master password authentication
- [ ] Backup and restore functionality
- [ ] Password expiry notifications
- [ ] Multi-user support
- [ ] GUI application (tkinter/PyQt)
- [ ] Cloud synchronization

---

## 🤝 Contributing

When adding features:
1. Maintain the modular structure
2. Follow existing code patterns
3. Add comprehensive docstrings
4. Include security considerations
5. Update this README with new features

---

## 📝 License

See [LICENSE](../../LICENSE) in the project root.

---

**Status**: ✅ Complete and Production-Ready
**Last Updated**: March 2024