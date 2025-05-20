import os
import time
import subprocess
from datetime import datetime

# Path where Roblox is usually installed
APPLICATIONS_DIR = "/Applications"
TARGET_PREFIX = "Roblox"

def set_permissions(block=True):
    for app_name in os.listdir(APPLICATIONS_DIR):
        if app_name.startswith(TARGET_PREFIX) and app_name.endswith(".app"):
            full_path = os.path.join(APPLICATIONS_DIR, app_name)
            chmod = "000" if block else "755"
            try:
                subprocess.run(["sudo", "chmod", "-R", chmod, full_path], check=True)
                print(f"{'Blocked' if block else 'Unblocked'}: {full_path}")
            except subprocess.CalledProcessError as e:
                print(f"Failed to set permissions on {full_path}: {e}")

def is_blocking_time():
    now = datetime.now()
    hour, minute = now.hour, now.minute
    # Block from 21:00 to 10:00
    return (hour >= 21) or (hour < 10) or (hour == 10 and minute == 0)

def main():
    last_state = None  # None, 'blocked', or 'unblocked'
    while True:
        should_block = is_blocking_time()
        if should_block and last_state != 'blocked':
            set_permissions(block=True)
            last_state = 'blocked'
        elif not should_block and last_state != 'unblocked':
            set_permissions(block=False)
            last_state = 'unblocked'
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()
