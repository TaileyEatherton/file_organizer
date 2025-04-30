#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

""" GLOBAL VARIABLES """
# Dictionary that maps categories to lists of file extensions.
# Used to determine which folder a file should be moved to based on its extension.
FILE_TYPES = {
    "Pictures": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".md", ".odt", ".rtf"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".webm"],
    "Audio": [".mp3", ".wav", ".flac", ".aac"],
    "Compressed": [".zip", ".tar", ".gz", ".7z", ".rar"],
    "Executables": [ ".exe", ".dll", ".app", ".iso", ".dep", ".rpm"],
    "Data_and_Code": [ ".tsv", ".ods", ".xls", ".xlsx", ".xml", ".csv", ".py", ".json", ".html", ".css", ".sh", ".bat", ".js", ".ini", ".toml", ".yaml"]
}
#OS indpenent paths
HOME_PATH = Path.home()
CURRENT_DIR_PATH = Path.cwd()

""" FUNCTIONS """

def create_folders(custom_folder=None):
    if custom_folder == None:
        for folder in FILE_TYPES.keys():
            (HOME_PATH / folder).mkdir(exist_ok=True)
    else:
        (HOME_PATH / custom_folder).mkdir(exist_ok=True)

def move_files(file):
    for folder, extensions in FILE_TYPES.items():
        if file.suffix.lower() in extensions:
            shutil.move(str(file), str(HOME_PATH / folder / file.name))
            break 


def organize_files(file_type=None):
    moved_files = []

    for file in CURRENT_DIR_PATH.iterdir():
        if file.is_file() and (file_type == None or file.suffix.lower() == file_type):
            move_files(file)
            moved_files.append(file)

    if moved_files:
        print(f"\nSuccess! {len(moved_files)} file(s) have been moved to their respective folders.")
    elif file_type:
        print((f"\nNo files with the extension '{file_type}' are found in the current directory."))


def Option_1():
    create_folders()
    organize_files()

def Option_2(file_type):
    create_folders()
    organize_files(file_type)
   
def Option_3(custom_folder, keyword):
    create_folders(custom_folder)
    for file in CURRENT_DIR_PATH.iterdir():
        if file.is_file() and keyword.lower() in file.name.lower():
            shutil.move(str(file), str(HOME_PATH / custom_folder / file.name))
            print(f"\nSuccess! {file.name} has been moved to {custom_folder}")

""" MAIN FUNCTION """

def main():
    while True:
        print("Option 1: Organize all files in the current directory by file type and move to its specified home folders. E.g. .txt to Documents, .jpg to Pictures, etc.")
        print("Option 2: Move specified file type in current directory to its respective home folder")
        print("Option 3: Create a custom folder and move all files containing a user-specified keyword in their name to that folder.")
        print("Option 4: Select 4 to exit.")

        try:
            user_option = int(input("\nSelect option 1, 2, 3, or 4: \n").strip())
            if user_option > 4 or user_option <= 0:
                print("\n Invalid Input. Please select 1-4. \n")
            elif user_option == 1:
                Option_1()
                break

            elif user_option == 2:
                user_specified_file_type = input("What file extension type would you like to move?(e.g. .txt, .pdf, .ini)").strip().lower()
                if not user_specified_file_type.startswith('.'):
                    user_specified_file_type = '.' + user_specified_file_type
                Option_2(user_specified_file_type)
                break

            elif user_option == 3:
                user_custom_folder = input("Folder name: ").strip()
                user_custom_keyword = input("Keyword: ").strip()
                Option_3(user_custom_folder, user_custom_keyword)
                break

            elif user_option == 4:
                print("Exiting Program...Goodbye:)")
                break

        except ValueError:
            print("\n Please enter a valid number 1-4 \n")

if __name__ == '__main__':
    main()