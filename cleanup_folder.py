import os

def cleanup_folder(directory=None):
    # Set the directory to the current working directory if none is specified
    if directory is None:
        directory = os.getcwd() + "/tex"

    # Get a list of all files in the specified directory
    files_in_directory = os.listdir(directory)

    # Loop through each file and check its extension
    for file_name in files_in_directory:
        # Check if the file ends with .log, .aux, or .out
        if file_name.endswith(('.log', '.aux', '.out', '.dvi', '.synctex.gz')):
            file_path = os.path.join(directory, file_name)
            try:
                # Delete the file
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Failed to delete {file_path}: {e}")

# Usage
cleanup_folder()  # Call function with the current working directory