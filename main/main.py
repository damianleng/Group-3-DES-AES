# main/main.py
import os
import sys

# Add the parent directory to the system path
current_file_path = os.path.abspath(__file__)
project_folder_path = os.path.dirname(os.path.dirname(current_file_path))
sys.path.append(project_folder_path)

def main():
    print("Welcome to Cryptography Project")


if __name__ == "__main__":
    main()