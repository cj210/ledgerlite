#!/usr/bin/env bash

# Exit immediately on unhandled errors
set -e

echo "==> Starting environment setup..."

# 1. Check if Python exists
if ! command -v python &> /dev/null; then
    echo "Error: Python is not installed or not in PATH."
    exit 1
fi

echo "==> Python found:"
python --version

# 2. Check for or create .venv
VENV_DIR=".venv"

if [ -d "$VENV_DIR" ]; then
    echo "==> Existing virtual environment '$VENV_DIR' found. Using it."
else
    echo "==> Creating virtual environment in '$VENV_DIR'..."
    python -m venv "$VENV_DIR"
fi

# 3. Activate .venv
# Source the activation script directly inside the executing shell
source "$VENV_DIR/bin/activate"
echo "==> Activated virtual environment."

# 4. Upgrade pip
echo "==> Upgrading pip..."
pip install --upgrade pip 

# 5. Check for requirements.txt and install packages
REQUIREMENTS_FILE="requirements.txt"

if [ ! -f "$REQUIREMENTS_FILE" ]; then
    echo "Warning: No $REQUIREMENTS_FILE found. Skipping package installation."
else
    echo "==> Installing requirements from $REQUIREMENTS_FILE..."
    pip install -r "$REQUIREMENTS_FILE"
fi

# 6. Final success message
echo "==> Bootstrap completed execution."
