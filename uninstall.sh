#!/data/data/com.termux/files/usr/bin/bash

echo "Uninstalling Secret Server..."

# Ensure PREFIX is defined (Termux base path)
PREFIX="/data/data/com.termux/files/usr"

# Remove launcher
if [ -f "$PREFIX/bin/secret-server" ]; then
    rm "$PREFIX/bin/secret-server"
    echo "Removed launcher."
fi

# Remove Termux:Boot script
BOOT_SCRIPT="$HOME/.termux/boot/secret-server.sh"
if [ -f "$BOOT_SCRIPT" ]; then
    rm "$BOOT_SCRIPT"
    echo "Removed Termux:Boot script."
fi

# Remove app directory
if [ -d "$HOME/secret-server" ]; then
    rm -rf "$HOME/secret-server"
    echo "Removed Secret Server directory."
fi

echo "Secret Server has been fully uninstalled."
