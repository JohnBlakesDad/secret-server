#!/usr/bin/env python3
"""
detect_hotspot.py

Run this on a client device (e.g., Laptop) connected to the Hotspot.
It identifies the Hotspot Host's IP address (the Gateway).

Usage:
  python3 detect_hotspot.py
"""
import socket
import struct
import sys

def get_default_gateway_linux():
    """
    Reads /proc/net/route to find the default gateway.
    Returns the IP address string of the gateway (the Hotspot Host).
    """
    try:
        with open("/proc/net/route") as f:
            for line in f.readlines():
                try:
                    iface, dest, gateway, flags, _, _, _, _, _, _, _ = line.strip().split()
                    
                    # Destination 00000000 is the default route
                    if dest != '00000000' or not int(flags, 16) & 2:
                        continue
                        
                    # Gateway is in little-endian hex
                    gateway_int = int(gateway, 16)
                    if gateway_int == 0:
                        continue
                        
                    return socket.inet_ntoa(struct.pack("<L", gateway_int))
                except (ValueError, IndexError):
                    continue
    except FileNotFoundError:
        print("Error: /proc/net/route not found. Are you on Linux?")
        return None
    return None

if __name__ == "__main__":
    print("--- Hotspot Host Detector ---")
    gateway_ip = get_default_gateway_linux()
    
    if gateway_ip:
        print(f"✅ Hotspot Host IP (Gateway): {gateway_ip}")
        print(f"🔗 Secret Server URL: http://{gateway_ip}:5001")
    else:
        print("❌ Could not detect default gateway.")
        print("   Ensure you are connected to the Wi-Fi Hotspot.")
