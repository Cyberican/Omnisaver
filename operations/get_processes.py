import math
import os
import psutil

print("Current Processes...\n")

for proc in psutil.process_iter(['pid', 'name', 'username']):
    try:
        process_info = proc.info
        print(f"PID: {process_info['pid']}, Name: {process_info['name']}, User: {process_info['username']}")
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

print("\nProcess listing complete.")