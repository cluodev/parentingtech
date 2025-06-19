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

def get_available_times_by_dayOfWeek():
    # This function is not used in the current implementation
    # but can be extended to return available times based on the day of the week.
    """Return a dictionary of available times for each day of the week."""
    # Example times are provided; adjust as needed.
    # Times are in 24-hour format as tuples of (start_hour, end_hour). half-hour represented as .5
    # The keys are the days of the week, and the values are lists of tuples.
    # This is a mock implementation. In a real scenario, you might fetch this from a configuration file or a database.
    # Each day has a list of tuples representing available time slots.
    # This is a placeholder implementation. 

    return {
        "Monday": [(10, 12), (16, 17), (17.5, 18.5)],
        "Tuesday": [(10, 12), (16, 17), (17.5, 18.5)],
        "Wednesday": [(10, 12), (16, 17), (17.5, 18.5)],
        "Thursday": [(10, 12), (16, 17), (17.5, 18.5)],
        "Friday": [(10, 12), (16, 17.5), (19.5, 21.5)],
        "Saturday": [(10, 12), (15, 16), (17, 18)],
        "Sunday": [(10, 12), (19.5, 20.5)]
    }

def is_blocking_time():
    """Check if the current time is within the blocking periods."""

    unblocking_times = get_available_times_by_dayOfWeek()
    current_time = datetime.now()
    current_day = current_time.strftime("%A")  # Get the full weekday name (e.g., 'Monday')
    current_hour = current_time.hour + current_time.minute / 60.0  # Convert to decimal hour

    for start, end in unblocking_times.get(current_day, []):
        if (current_hour > start and current_hour < end) or (current_hour == start and current_time.minute == 0):
            return False  # Not blocking time

    return True  # Blocking time

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
        time.sleep(30)  # Check every 30 seconds

if __name__ == "__main__":
    main()
