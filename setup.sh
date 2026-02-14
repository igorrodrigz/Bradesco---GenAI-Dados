#!/bin/bash
# Setup script for Agent Memory Configuration System

echo "=== Agent Memory Configuration System - Setup ==="
echo ""

# Check Python version
echo "Checking Python version..."
python_version=$(python3 --version 2>&1)
echo "Found: $python_version"
echo ""

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv
echo "✓ Virtual environment created"
echo ""

# Activate virtual environment
echo "To activate the virtual environment, run:"
echo "  source venv/bin/activate  (Linux/Mac)"
echo "  venv\\Scripts\\activate   (Windows)"
echo ""

# Install dependencies
echo "Installing dependencies..."
if [ -f "venv/bin/python" ]; then
    venv/bin/pip install -r requirements.txt
    echo "✓ Dependencies installed"
else
    echo "⚠ Please activate the virtual environment and run: pip install -r requirements.txt"
fi
echo ""

# Setup .env file
if [ ! -f ".env" ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "✓ .env file created"
    echo "⚠ Please edit .env and add your OpenAI API key"
else
    echo "✓ .env file already exists"
fi
echo ""

echo "=== Setup Complete ==="
echo ""
echo "Next steps:"
echo "1. Activate virtual environment: source venv/bin/activate"
echo "2. Edit .env file and add your OPENAI_API_KEY"
echo "3. Run examples: python examples/basic_usage.py"
echo ""
