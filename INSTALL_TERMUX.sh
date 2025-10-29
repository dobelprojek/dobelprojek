#!/data/data/com.termux/files/usr/bin/bash

# Script instalasi otomatis untuk Termux
# WhatsApp Number Tracker

echo "╔══════════════════════════════════════════╗"
echo "║  WhatsApp Number Tracker - Installer    ║"
echo "║  untuk Termux                            ║"
echo "╚══════════════════════════════════════════╝"
echo ""

# Update packages
echo "📦 Updating packages..."
pkg update -y

# Install Python jika belum ada
echo "🐍 Checking Python installation..."
if ! command -v python &> /dev/null; then
    echo "Installing Python..."
    pkg install python -y
else
    echo "✅ Python already installed"
fi

# Install pip jika belum ada
echo "📦 Checking pip installation..."
if ! command -v pip &> /dev/null; then
    echo "Installing pip..."
    pkg install python-pip -y
else
    echo "✅ pip already installed"
fi

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Berikan permission
echo "🔐 Setting permissions..."
chmod +x wa_tracker.py

echo ""
echo "╔══════════════════════════════════════════╗"
echo "║  ✅ Instalasi Selesai!                   ║"
echo "╚══════════════════════════════════════════╝"
echo ""
echo "Cara menjalankan:"
echo "  python wa_tracker.py"
echo ""
echo "atau:"
echo "  ./wa_tracker.py"
echo ""
