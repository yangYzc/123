# Branch 1 - Utilities
# Utility functions for branch 1

import datetime

def get_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def format_message(msg):
    return f"[BRANCH1] {get_current_time()}: {msg}"

def validate_input(data):
    if not data:
        return False, "Data is empty"
    if len(data) < 3:
        return False, "Data too short"
    return True, "Valid data"