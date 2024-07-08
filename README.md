

# File Organizer Scripts

This repository contains a collection of Python scripts designed to help you organize and manage files in your system. Currently, the following scripts are included:

- `organize_it.py`: Organizes files in a specified folder based on their file types and handles duplicates.
- `move2trash.py`: Moves specified files or folders to the trash.

## Scripts

### organize_it.py

This script organizes files in a specified folder (e.g., `/Users/gigi/Downloads`) into subfolders based on their file types (e.g., images, documents, spreadsheets). It also identifies and moves duplicate files to a `Duplicates` folder.

#### Features

- **Organizes Files by Type**: Maps common file extensions to folders like `jpeg`, `images`, `documents`, etc.
- **Handles Duplicates**: Moves duplicate files to a `Duplicates` folder, ensuring unique filenames to prevent overwriting.
- **Recursive Handling**: Processes files in all subdirectories of the specified folder.

#### Usage

1. **Set the Folder Path**: Modify the script to specify the folder you want to organize.
    ```python
    folder_path = "/Users/gigi/Downloads"  # Set the fixed folder path here
    ```
2. **Run the Script**:
    ```sh
    python3 organize_it.py
    ```

### move2trash.py

This script moves specified files or folders to the trash, helping you manage unwanted files easily.

#### Features

- **Move to Trash**: Safely moves files or folders to the trash instead of permanently deleting them.

#### Usage

1. **Specify the Files/Folders**: Modify the script to specify the files or folders you want to move to the trash.
2. **Run the Script**:
    ```sh
    python3 move2trash.py
    ```
### plotgenerator
tbd.
## Future Scripts

This repository is a work in progress. More scripts to help with file management and organization will be added soon. Stay tuned!

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or new features to add, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to customize this `README.md` further based on your needs and add specific details about the `move2trash.py` script if there are particular functionalities or instructions you'd like to highlight.
