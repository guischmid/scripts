import os
import hashlib
import shutil

# Mapping of file extensions to their respective types
FILE_TYPE_MAP = {
    '.jpg': 'jpeg',
    '.jpeg': 'jpeg',
    '.png': 'images',
    '.gif': 'images',
    '.bmp': 'images',
    '.pdf': 'documents',
    '.doc': 'documents',
    '.docx': 'documents',
    '.xls': 'spreadsheets',
    '.xlsx': 'spreadsheets',
    '.ppt': 'presentations',
    '.pptx': 'presentations',
    '.txt': 'text',
    '.csv': 'spreadsheets',
    # Add more mappings as needed
}

import hashlib

def get_file_hash(file_path):
    """
    Calculate the SHA256 hash of a file.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The SHA256 hash of the file.

    """
    with open(file_path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def ensure_unique_filename(folder_path, filename):
    """
    Ensures that the given filename is unique within the specified folder path.
    
    Args:
        folder_path (str): The path to the folder where the file should be saved.
        filename (str): The original filename.
    
    Returns:
        str: A unique filename that does not exist in the specified folder path.
    """
    base, extension = os.path.splitext(filename)
    counter = 1
    unique_filename = filename
    while os.path.exists(os.path.join(folder_path, unique_filename)):
        unique_filename = f"{base}_{counter}{extension}"
        counter += 1
    return unique_filename

def get_destination_folder(extension):
    """
    Returns the destination folder based on the given file extension.

    Parameters:
    extension (str): The file extension to map to a destination folder.

    Returns:
    str: The destination folder corresponding to the given file extension. If the extension is not mapped, 'others' is returned as the default.

    """
    return FILE_TYPE_MAP.get(extension, 'others')  # Default to 'others' if the extension is not mapped

import os
import shutil

def organize_and_move_duplicates(folder_path):
    """
    Organizes files in the specified folder by moving them to destination folders based on their file types.
    Duplicates are moved to a separate "Duplicates" folder.

    Args:
        folder_path (str): The path to the folder containing the files to be organized.

    Returns:
        None
    """
    # Create a dictionary to store destination folders based on file types
    type_folders = {}

    # Create the "Duplicates" folder if it doesn't exist
    duplicates_folder = os.path.join(folder_path, 'Duplicates')
    os.makedirs(duplicates_folder, exist_ok=True)

    # Create a dictionary to store file hashes
    file_hashes = {}

    # Iterate through files in the folder
    for root, _, files in os.walk(folder_path):
        if root == duplicates_folder:
            continue
        for filename in files:
            file_path = os.path.join(root, filename)
            # Get the file extension
            _, extension = os.path.splitext(filename)
            extension = extension.lower()  # Convert extension to lowercase
            
            # Determine the destination folder
            file_type = get_destination_folder(extension)
            if file_type in type_folders:
                destination_folder = type_folders[file_type]
            else:
                destination_folder = os.path.join(folder_path, file_type)
                os.makedirs(destination_folder, exist_ok=True)
                type_folders[file_type] = destination_folder
            
            # Calculate the file hash
            file_hash = get_file_hash(file_path)
            
            # Check for duplicates
            if file_hash in file_hashes:
                # File is a duplicate, move it to the "Duplicates" folder with a unique name
                unique_filename = ensure_unique_filename(duplicates_folder, filename)
                shutil.move(file_path, os.path.join(duplicates_folder, unique_filename))
                print(f"Moved duplicate file {filename} to Duplicates folder as {unique_filename}.")
            else:
                # Store the file hash
                file_hashes[file_hash] = filename
                # Move the file to the destination folder with a unique name
                unique_filename = ensure_unique_filename(destination_folder, filename)
                shutil.move(file_path, os.path.join(destination_folder, unique_filename))
                print(f"Moved {filename} to {destination_folder} as {unique_filename}.")

if __name__ == "__main__":
    folder_path = "/Users/gigi/Downloads"  # Set the fixed folder path here
    if os.path.isdir(folder_path):
        organize_and_move_duplicates(folder_path)
    else:
        print("Invalid folder path. Please enter a valid directory.")