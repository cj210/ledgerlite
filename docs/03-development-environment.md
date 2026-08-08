# Development Environment

## Environment Philosophy

The development environment is divided into two layers.

### Machine Layer

Contains tools shared across all projects.

Examples:

- Git
- Python
- SQLite
- SSH

### Project Layer

Contains dependencies specific to LedgerLite.

Examples:

- FastAPI
- SQLAlchemy
- Alembic
- Pytest

Project dependencies are installed inside a Python virtual environment (.venv) to isolate them from other projects.

## Development Machine

### 1. Tool: Arch Linux VM

#### Purpose
Development is performed inside an isolated Arch Linux virtual machine to provide a reproducible Linux environment and avoid affecting the host operating system.

#### Machine Installation
[Virtual Machine Installation Guide](https://docs.google.com/document/d/15e1xeESCXTM7htRZCBT5YmAGfnxytVrxOZtdiXI5UOo/edit?tab=t.bxmq9zuuca7x)

#### Verification
```bash
cat /etc/os-release
cat /etc/arch-release
cat /etc/issue
```

### 2. Tool: SSH

#### Purpose
To secure login from host machine into VMs. 

#### Machine Installation
```bash
sudo pacman -S openssh
```

#### Verification
```bash
sudo systemctl status sshd
```

#### Common Operations
```bash
sudo systemctl enable --now sshd
sudo systemctl restart sshd
```

### 3. Tool: Git

#### Purpose
Version control. Project use github repository. 

#### Machine Installation
```bash
sudo pacman -S git
```

#### Verification
```bash
git --version
```

#### Common Operations
```bash
git config --global user.name
git config --global user.email
git config --global init.defaultBranch
git clone https://accesstoken@remaingithttplink
git merge --squash branch_name
```

### 4. Tool: Python

#### Purpose
Python is the primary programming language and runtime used to develop and execute LedgerLite. It also provides the standard library and tools such as venv.

#### Machine Installation
```bash
sudo pacman -S python
```

#### Verification
```bash
python --version
```

#### Common Operations
```bash
```

### 5. Tool: Sqlite

#### Purpose
Required as local database engine and CLI for inspection/debugging

#### Machine Installation
```bash
sudo pacman -S sqlite
```

#### Verification
```bash
sqlite3 --version
```

#### Common Operations
```bash
sqlite3
.help
.quit
.tables
.schema
.headers on
.mode column
```

### 6. Tool: Pip

#### Purpose
Pip is Python's package manager. It installs and manages project-specific dependencies inside the virtual environment.

#### Machine Installation
```bash
sudo pacman -S python-pip
```

#### Verification
```bash
pip --version
```

#### Common Operations
```bash
pip install <package name>
```

### 7. Tool: Node.js

#### Purpose

Node.js provides the JavaScript runtime required for frontend development and frontend tooling.

#### Machine Installation

    sudo pacman -S nodejs

#### Verification

    node --version

#### Common Operations

    node

### 8. Tool: npm

#### Purpose

npm is the package manager used to install and manage frontend project dependencies.

#### Machine Installation

npm is installed with Node.js.

#### Verification

    npm --version

#### Common Operations

    npm install
    npm install <package>
    npm install -D <package>
    npm run <script>

## Project Dependencies

LedgerLite maintains dependencies separately for the backend and frontend.

### Backend

Python dependencies are managed using the project virtual environment.

The dependency list is maintained in:

    requirements.txt

The file should be updated as backend dependencies evolve.

### Frontend

JavaScript dependencies are managed using npm.

Dependency definitions are maintained in:

    ui/package.json

Exact dependency resolution is maintained in:

    ui/package-lock.json

Both files are committed to the repository so that the frontend environment can be reproduced consistently.
