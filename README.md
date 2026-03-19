# Py Scripts for Life

A collection of practical Python utilities and tools for everyday tasks.

## 🌟 Projects

### Password Manager ✅
A secure command-line password manager with encryption support.

**Features:**
- Generate secure random passwords with customizable options
- Store passwords with website, email, and timestamp
- Encrypt/decrypt passwords using Fernet (industry-standard)
- Interactive CLI interface

**Status**: Complete and production-ready

### YouTube to MP3 🚧
Download YouTube videos and convert them to MP3 audio files.

**Status**: In development (placeholder)

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Poetry

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd py-scripts-for-life
```

2. Install dependencies:
```bash
poetry install
```

### Running the Application

```bash
poetry run python src/main.py
```

Select a tool from the menu to get started.

---

## 📁 Project Structure

```
py-scripts-for-life/
├── README.md                    # This file
├── LICENSE                      # MIT License
├── pyproject.toml              # Poetry configuration
├── poetry.lock                 # Dependency lock file
│
├── src/
│   ├── main.py                 # Application entry point
│   ├── password_manager/       # Password Manager module
│   │   ├── password_generator.py
│   │   ├── README.md
│   │   └── __init__.py
│   ├── yt-to-mp3/             # YouTube to MP3 module (placeholder)
│   │   ├── README.md
│   │   └── __init__.py
│   └── shared/                # Shared utilities
│       ├── graphics.py        # UI formatting
│       └── __init__.py
│
├── tests/                     # Test directory
└── context/                   # Project summary
```

---

## 🛠️ Tech Stack

- **Python** 3.10+ - Programming language
- **Poetry** - Dependency management
- **Cryptography** - Fernet encryption library

---

## 📚 Documentation

- **Password Manager**: [src/password_manager/README.md](./src/password_manager/README.md)
- **YouTube to MP3**: [src/yt-to-mp3/README.md](./src/yt-to-mp3/README.md)
- **Project Summary**: [context/README.md](./context/README.md)

---

## 🔐 Security

**Password Manager Security:**
- All passwords encrypted with Fernet (symmetric encryption)
- Encryption key stored in `outputs/key.key`
- Key file excluded from version control (.gitignore)
- No hardcoded secrets or credentials
- Proper resource cleanup with context managers

**Important**: Do not lose your `key.key` file. Without it, stored passwords cannot be decrypted.

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

---

## 👤 Author

**Benedict Angelo**
- GitHub: [@BenedictAngelo](https://github.com/BenedictAngelo)
- Email: BenedictAngelo@protonmail.com

---

## 🤝 Contributing

Contributions are welcome! Follow the existing code patterns and documentation standards when adding new features.

---

**Status**: Active Development | **Last Updated**: March 2024