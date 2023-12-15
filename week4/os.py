import os
import shutil
import time

def is_file_updated(file_path):
    """Check if a file has been created or modified in the last 24 hours."""
    twenty_four_hours_ago = time.time() - 24 * 60 * 60
    file_stats = os.stat(file_path)

    return file_stats.st_mtime > twenty_four_hours_ago or file_stats.st_ctime > twenty_four_hours_ago

def update_file(file_path):
    """Update the identified file by appending a timestamp to its content."""
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()).lstrip("0")
    with open(file_path, 'a') as file:
        file.write(f"\nUpdated at: {current_time}")

def create_last_24hours_folder():
    """Create the 'last_24hours' folder if it doesn't exist."""
    folder_name = "last_24hours"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def move_file_to_last_24hours(file_path):
    """Move the identified file to the 'last_24hours' folder."""
    folder_name = "last_24hours"
    shutil.move(file_path, folder_name)

def main():
    # Get the current directory
    current_directory = os.getcwd()

    # Create the 'last_24hours' folder if it doesn't exist
    create_last_24hours_folder()

    # List all files in the current directory
    files = os.listdir(current_directory)

    # Iterate over the files and process the ones updated in the last 24 hours
    for file in files:
        file_path = os.path.join(current_directory, file)
        if os.path.isfile(file_path) and is_file_updated(file_path):
            # Update the identified file
            update_file(file_path)

            # Move the updated file to the 'last_24hours' folder
            move_file_to_last_24hours(file_path)

if __name__ == "__main__":
    main()
