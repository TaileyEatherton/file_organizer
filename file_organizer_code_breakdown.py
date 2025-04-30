#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

""" GLOBAL VARIABLES """
# This dictionary defines file categories and the corresponding file extensions.
# Each category (Pictures, Documents, etc.) has a list of file extensions that belong to it.
FILE_TYPES = {
    "Pictures": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],  # Image files
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".md", ".odt", ".rtf"],    # Document files
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".webm"],                      # Video files
    "Audio": [".mp3", ".wav", ".flac", ".aac"],                               # Audio files
    "Compressed": [".zip", ".tar", ".gz", ".7z", ".rar"],                     # Compressed files
    "Executables": [".exe", ".dll", ".app", ".iso", ".dep", ".rpm"],          # Executable files
    "Data_and_Code": [".tsv", ".ods", ".xls", ".xlsx", ".xml", ".csv", ".py", ".json", ".html", ".css", ".sh", ".bat", ".js", ".ini", ".toml", ".yaml"]  # Code and data files
}

# Define the paths for the home directory and current working directory.
HOME_PATH = Path.home()  # Gets the path to the user's home directory.
CURRENT_DIR_PATH = Path.cwd()  # Gets the current working directory (where the script is executed).

""" FUNCTIONS """

def create_folders(custom_folder=None):
    """
    This function creates the necessary folders (Pictures, Documents, etc.) inside the home directory.
    If a custom folder name is provided, it creates that specific folder instead.
    """
    if custom_folder is None:
        # Creates default folders for each category defined in FILE_TYPES.
        for folder in FILE_TYPES.keys():
            (HOME_PATH / folder).mkdir(exist_ok=True)  # 'exist_ok=True' prevents an error if the folder already exists.
    else:
        # Creates a custom folder if a custom name is provided.
        (HOME_PATH / custom_folder).mkdir(exist_ok=True)

def move_files(file):
    """
    This function moves the given file to the appropriate folder based on its extension.
    It iterates through the file categories and checks the file extension.
    """
    for folder, extensions in FILE_TYPES.items():
        if file.suffix.lower() in extensions:  # Checks if the file's extension matches any of the categories.
            # Moves the file to the appropriate folder in the home directory.
            shutil.move(str(file), str(HOME_PATH / folder / file.name))
            break  # Exit the loop once the file is moved.

def organize_files(file_type=None):
    """
    This function organizes files based on their extension.
    If a file_type is specified, it only moves files with that extension.
    If no file_type is provided, it organizes all files.
    """
    moved_files = []  # List to track which files are moved.

    # Iterates through all files in the current directory.
    for file in CURRENT_DIR_PATH.iterdir():
        if file.is_file() and (file_type is None or file.suffix.lower() == file_type):
            move_files(file)  # Moves the file if it's of the right type.
            moved_files.append(file)  # Adds the file to the moved_files list.

    # Provides feedback on how many files were moved.
    if moved_files:
        print(f"\nSuccess! {len(moved_files)} file(s) have been moved to their respective folders.")
    elif file_type:
        print(f"\nNo files with the extension '{file_type}' are found in the current directory.")

def Option_1():
    """
    Option 1: Organize all files in the current directory by their type and move them to respective folders.
    """
    create_folders()  # Creates default folders (Pictures, Documents, etc.).
    organize_files()  # Organizes and moves all files.

def Option_2(file_type):
    """
    Option 2: Organize files based on a specific extension. Only moves files matching the provided extension.
    """
    create_folders()  # Creates default folders (Pictures, Documents, etc.).
    organize_files(file_type)  # Organizes and moves files of the given extension.

def Option_3(custom_folder, keyword):
    """
    Option 3: Creates a custom folder and moves files that contain the specified keyword in their name to that folder.
    """
    create_folders(custom_folder)  # Creates the custom folder.
    for file in CURRENT_DIR_PATH.iterdir():
        if file.is_file() and keyword.lower() in file.name.lower():  # Checks if the file contains the keyword.
            shutil.move(str(file), str(HOME_PATH / custom_folder / file.name))  # Moves the file to the custom folder.
            print(f"\nSuccess! {file.name} has been moved to {custom_folder}")

""" MAIN FUNCTION """

def main():
    """
    The main function that drives the program. It shows the user options, takes input, and calls the respective functions.
    """
    while True:
        # Menu displaying the different options for organizing files.
        print("Option 1: Organize all files in the current directory by file type and move to its specified home folders. E.g. .txt to Documents, .jpg to Pictures, etc.")
        print("Option 2: Move specified file type in current directory to its respective home folder")
        print("Option 3: Create a custom folder and move all files containing a user-specified keyword in their name to that folder.")
        print("Option 4: Select 4 to exit.")

        try:
            # Prompts the user to select an option.
            user_option = int(input("\nSelect option 1, 2, 3, or 4: \n").strip())
            
            # Checks if the input is valid (1-4).
            if user_option > 4 or user_option <= 0:
                print("\n Invalid Input. Please select 1-4. \n")
            elif user_option == 1:
                Option_1()  # Calls Option 1 function.
                break

            elif user_option == 2:
                # Asks the user for a specific file type to organize.
                user_specified_file_type = input("What file extension type would you like to move?(e.g. .txt, .pdf, .ini)").strip().lower()
                if not user_specified_file_type.startswith('.'):  # Adds '.' if not provided.
                    user_specified_file_type = '.' + user_specified_file_type
                Option_2(user_specified_file_type)  # Calls Option 2 function.
                break

            elif user_option == 3:
                # Asks the user for a custom folder name and keyword.
                user_custom_folder = input("Folder name: ").strip()
                user_custom_keyword = input("Keyword: ").strip()
                Option_3(user_custom_folder, user_custom_keyword)  # Calls Option 3 function.
                break

            elif user_option == 4:
                print("Exiting Program...Goodbye:)")  # Exits the program.
                break

        except ValueError:
            print("\n Please enter a valid number 1-4 \n")  # Error handling for invalid input.

# This ensures the script runs when executed directly (but not when imported as a module).
if __name__ == '__main__':
    main()
