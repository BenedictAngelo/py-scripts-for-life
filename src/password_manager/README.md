# Password Manager

A secure command-line password manager with encryption support using Fernet.

## 🌟 Features

- **Password Generation**: Create secure random passwords with customizable length and character types
- **Password Storage**: Save passwords with associated website and email information
- **Encryption**: All passwords are encrypted using Fernet (symmetric encryption)
- **View Passwords**: Retrieve and decrypt stored passwords
- **User-Friendly**: Interactive command-line interface with clear prompts

## 🛠️ Tech Stack

- **Python** 3.10+ - Programming language
- **Cryptography** - Fernet encryption for secure password storage

## 📁 Project Structure

```
password_manager/
├── README.md               # This file
├── password_generator.py   # Password generation and encryption implementation
├── modes.py                # Mode select for what to do for the app
├── app.py                  # Wrapper for all the components
├── __init__.py             # Module initialization
outputs/
├── key.key                 # Encryption key (auto-generated)
└── passwords.txt           # Encrypted password storage
```

## 📋 Components Overview

### PasswordGenerator
Generates secure random passwords based on specified criteria:
- Customizable password length
- Optional digit inclusion
- Optional special character inclusion
- Automatic encryption of generated passwords

### PasswordManager
Manages password storage and metadata:
- Stores website, email, password, and creation timestamp
- Inherits password generation from PasswordGenerator
- Provides getter methods for stored data

### PasswordMode
Handles user interaction modes:
- **View Mode**: Display all stored passwords (decrypted)
- **Add Mode**: Create and store new passwords

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- cryptography library
- Parent project poetry environment

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
1. Create a `key.key` file (encryption key) - **keep this safe!**
2. Create a `passwords.txt` file (encrypted password storage)

**Important**: Do not share or lose the `key.key` file. Without it, stored passwords cannot be decrypted.

---

## 💻 Usage

### Adding a Password

1. Select "add" mode from the menu
2. Enter the website/service name
3. Enter your email address
4. Specify password length (digits only)
5. Choose whether to include digits (y/n)
6. Choose whether to include special characters (y/n)
7. Password is generated, encrypted, and saved

### Viewing Passwords

1. Select "view" mode from the menu
2. All stored passwords are displayed in decrypted format
3. Shows: Website, Email, Password, Creation Time

---

## 🔐 Security Notes

- Passwords are encrypted using Fernet (symmetric encryption)
- The `key.key` file is required to decrypt passwords
- Do not commit `key.key` or `passwords.txt` to version control
- These files are already in `.gitignore`
- Store `key.key` in a secure location

---

## 📂 File Descriptions

| File | Purpose |
|------|---------|
| `password_manager.py` | Core implementation with PasswordGenerator, PasswordManager, and PasswordMode classes |
| `key.key` | Encryption key (auto-generated on first run) |
| `passwords.txt` | Encrypted password storage (pipe-delimited format) |

---

## 🔄 Data Format

Passwords are stored in `passwords.txt` as pipe-delimited records:
```
website|email|encrypted_password|timestamp
```

Example:
```
google.com|user@example.com|gAAAAABl...|03:45:22 Mon Mar-18-2024
```

---

## 🐛 Known Limitations

- Passwords are stored locally in a text file (not a database)
- No search functionality yet
- No password strength indicator
- Single encryption key for all passwords

---

## 📚 Development Documentation

For technical details about the implementation and recent refactoring, see:
- `context/QUICK_REFERENCE.md` - Overview of code changes
- `context/TESTING_CHECKLIST.md` - Testing guide
- `context/DETAILED_CHANGES.md` - Code comparison

---

## 🚀 Future Enhancements

- [ ] Database support (SQLite)
- [ ] Password search functionality
- [ ] Password strength indicator
- [ ] Password update/delete features
- [ ] Backup and restore functionality
- [ ] Master password authentication
- [ ] Unit tests

---

## 🤝 Contributing

Improvements and bug reports are welcome!

---

## 📝 License

See [LICENSE](../../LICENSE) in the project root.

---

**Status**: ✅ Complete and Production-Ready
**Last Updated**: March 2024
