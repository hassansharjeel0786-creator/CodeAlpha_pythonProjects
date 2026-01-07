import os
import shutil

def main():
    # Prompt user for source and destination folder paths
    source_folder = input("Enter the source folder path (where .jpg files are located): ").strip()
    dest_folder = input("Enter the destination folder path (where .jpg files will be moved): ").strip()

    # Check if source folder exists
    if not os.path.exists(source_folder):
        print(f"Error: Source folder '{source_folder}' does not exist.")
        return

    # Check if source is a directory
    if not os.path.isdir(source_folder):
        print(f"Error: '{source_folder}' is not a directory.")
        return

    # Create destination folder if it doesn't exist
    if not os.path.exists(dest_folder):
        try:
            os.makedirs(dest_folder)
            print(f"Created destination folder: {dest_folder}")
        except OSError as e:
            print(f"Error creating destination folder: {e}")
            return

    # Get list of .jpg files in source folder
    jpg_files = [f for f in os.listdir(source_folder) if f.lower().endswith('.jpg')]

    if not jpg_files:
        print("No .jpg files found in the source folder.")
        return

    # Move each .jpg file to destination folder
    moved_count = 0
    for file in jpg_files:
        source_path = os.path.join(source_folder, file)
        dest_path = os.path.join(dest_folder, file)
        try:
            shutil.move(source_path, dest_path)
            print(f"Moved: {file}")
            moved_count += 1
        except shutil.Error as e:
            print(f"Error moving {file}: {e}")

    print(f"Task completed successfully. Moved {moved_count} .jpg files.")

if __name__ == "__main__":
    main()
