# Py Scripts for Life

A collection of practical Python utilities and tools for everyday tasks.

## 📚 Projects Overview

This repository contains multiple standalone Python projects. Each module has its own documentation and can be used independently.

### Available Projects

#### 1. [Password Manager](./src/password_manager/README.md)
A secure command-line password manager with encryption support.
- Generate secure random passwords
- Store passwords with website and email information
- Encrypt/decrypt passwords using Fernet
- View stored passwords

**Status**: ✅ Complete

#### 2. [YouTube to MP3](./src/yt-to-mp3/README.md)
Download YouTube videos and convert them to MP3 audio files.

**Status**: 🚧 In Development

#### 3. Future Projects
More utilities coming soon!

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Poetry (for dependency management)

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

Start the main menu:
```bash
poetry run python src/main.py
```

This will display a menu where you can select which tool to use.

---

## 📁 Project Structure

```
py-scripts-for-life/
├── src/
│   ├── main.py                          # Main entry point
│   ├── password_manager/
│   │   ├── README.md                    # Password Manager docs
│   │   ├── password_manager.py          # Core implementation
│   │   └── __init__.py
│   ├── yt-to-mp3/
│   │   ├── README.md                    # YouTube to MP3 docs
│   │   └── [project files]
│   ├── shared/
│   │   ├── __init__.py
│   │   └── graphics.py                  # Shared UI components
│   └── [other projects]
├── context/                             # Development documentation
├── pyproject.toml                       # Project configuration
├── poetry.lock                          # Dependency lock file
└── README.md                            # This file
```

---

## 🛠️ Tech Stack

- **Python** 3.10+ - Programming language
- **Poetry** - Dependency management
- **Cryptography** - Password encryption (Password Manager)

---

## 📖 Module Documentation

For detailed information about each project, see:

- **Password Manager**: [./src/password_manager/README.md](./src/password_manager/README.md)
- **YouTube to MP3**: [./src/yt-to-mp3/README.md](./src/yt-to-mp3/README.md)

---

## 🔧 Development

### Development Documentation

Technical documentation and refactoring notes are available in the `context/` directory:
- `context/QUICK_REFERENCE.md` - Quick overview of changes
- `context/TESTING_CHECKLIST.md` - Testing guide
- `context/DETAILED_CHANGES.md` - In-depth code analysis

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork and submit pull requests.

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

---

## 👤 Author

**Benedict Angelo**
- GitHub: [@BenedictAngelo](https://github.com/BenedictAngelo)
- Email: BenedictAngelo@protonmail.com

---

**Last Updated**: March 2024
**Status**: Active Development