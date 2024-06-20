#!/usr/bin/env python3

import os
import time
from datetime import datetime
from send2trash import send2trash

def move_old_files_to_trash(folder_path, days=30):
    """
    Moves files older than 'days' days to the trash in the given folder path.

    Parameters:
    folder_path (str): Path to the folder.
    days (int): Number of days to determine old files. Default is 30 days.
    """
    now = time.time()
    cutoff = now - (days * 86400)  # 86400 seconds in a day

    if not os.path.exists(folder_path):
        print(f"The folder {folder_path} does not exist.")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if os.path.isfile(file_path):
            file_modified_time = os.path.getmtime(file_path)
            file_modified_date = datetime.fromtimestamp(file_modified_time)
            print(f"Checking {file_path}, last modified on {file_modified_date}")

            if file_modified_time < cutoff:
                try:
                    send2trash(file_path)
                    print(f"Moved {file_path} to the trash.")
                except Exception as e:
                    print(f"Failed to move {file_path} to the trash. Reason: {e}")
        else:
            print(f"{file_path} is not a file.")

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    move_old_files_to_trash(folder_path)