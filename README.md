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

**Status**: On going and production-ready

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

#### Development Mode (Recommended)
For development, use `poetry run` - changes are reflected immediately without rebuilding:

```bash
poetry run py-scripts-for-life
```

#### Poetry Shell Mode
Activate the poetry virtual environment for the current terminal session:

```bash
poetry shell
py-scripts-for-life
```

#### Global Installation (Production)
For a global system-wide installation, use `pipx`:

1. Build the distribution:
```bash
poetry build
```

2. Install globally with pipx:
```bash
pipx install dist/py_scripts_for_life-0.1.0-py3-none-any.whl
```

3. Use from anywhere:
```bash
py-scripts-for-life
```

**Note**: After making code changes, rebuild and reinstall with pipx to use the updated version.

---

Select a tool from the menu to get started.

---

## 📦 Build & Distribution

### Development Workflow

For active development, use editable installation - **changes are reflected immediately without rebuilding**:

```bash
# One-time setup (if not already done)
pip install -e .

# Then make changes and test
poetry run py-scripts-for-life
```

Changes to your source code are automatically picked up - no rebuild needed!

### Production Workflow

To build and distribute the application:

#### Step 1: Build Distribution Packages

```bash
poetry build
```

This creates:
- `dist/py_scripts_for_life-0.1.0.tar.gz` - Source distribution
- `dist/py_scripts_for_life-0.1.0-py3-none-any.whl` - Wheel (binary) distribution

#### Step 2: Install Globally (with pipx)

Install globally on your system:

```bash
pipx install dist/py_scripts_for_life-0.1.0-py3-none-any.whl
```

Or install from PyPI when published:

```bash
pipx install py-scripts-for-life
```

#### Step 3: Use Anywhere

```bash
# Available from any directory in your system
py-scripts-for-life
```

### Updating Production Installation

After making code changes and rebuilding:

```bash
poetry build
pipx install --force dist/py_scripts_for_life-0.1.0-py3-none-any.whl
```

### Comparison: Development vs Production

| Aspect | Development | Production |
|--------|---|---|
| **Command** | `poetry run py-scripts-for-life` | `py-scripts-for-life` (global) |
| **Location** | Project directory | Anywhere |
| **Rebuild on Changes** | ❌ No | ✅ Yes |
| **Virtual Env** | Poetry-managed | Pipx-managed |
| **Use Case** | Active coding | Distribution/End-users |
| **Installation** | `pip install -e .` | `pipx install` |

### Editable Install Details

The `pip install -e .` command creates a "development mode" installation that:
- ✅ Links to your source code instead of copying it
- ✅ Allows immediate testing of changes
- ✅ Installs the `py-scripts-for-life` command
- ✅ Tracks all dependencies from `pyproject.toml`

Perfect for iterative development!

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
│   └── py-scripts-for-life/    # Main package namespace
│       ├── main.py             # Application entry point
│       │
│       ├── password_manager/   # Password Manager module
│       │   ├── README.md
│       │   ├── app.py          # Main application logic
│       │   ├── modes.py        # Mode handlers
│       │   ├── password_generator.py  # Core implementation
│       │   └── __init__.py
│       │
│       ├── yt-to-mp3/          # YouTube to MP3 module (placeholder)
│       │   ├── README.md
│       │   └── __init__.py
│       │
│       └── shared/             # Shared utilities
│           ├── graphics.py     # UI formatting
│           └── __init__.py
│
├── tests/                      # Test directory
├── context/                    # Project summary
└── outputs/                    # Runtime data directory
    ├── key.key                 # Encryption key (auto-generated)
    └── passwords.txt           # Encrypted passwords (auto-generated)
```

---

## 🛠️ Tech Stack

- **Python** 3.10+ - Programming language
- **Poetry** - Dependency management and build tool
- **Cryptography** - Fernet encryption library
- **requests** - HTTP library

---

## 📚 Documentation

- **Password Manager**: [src/py-scripts-for-life/password_manager/README.md](./src/py-scripts-for-life/password_manager/README.md)
- **YouTube to MP3**: [src/py-scripts-for-life/yt-to-mp3/README.md](./src/py-scripts-for-life/yt-to-mp3/README.md)

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

**Status**: Active Development | **Last Updated**: 2024