import os
import shutil

def cleanup_folder(delete_folder=False):
    # Define the directory
    directory = os.path.join(os.getcwd(), "tex")
    
    # Check if the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory created: {directory}")
        return  # Exit the function since there's nothing to clean up

    if delete_folder:
        try:
            # Delete the entire directory and its contents
            shutil.rmtree(directory)
            print(f"Directory deleted: {directory}")
        except Exception as e:
            print(f"Failed to delete directory {directory}: {e}")
        return  # Exit the function after deleting the folder

    # Get a list of all files in the specified directory
    files_in_directory = os.listdir(directory)

    # Loop through each file and check its extension
    for file_name in files_in_directory:
        # Check if the file ends with .log, .aux, .out, .dvi, or .synctex.gz
        if file_name.endswith(('.log', '.aux', '.out', '.dvi', '.synctex.gz')):
            file_path = os.path.join(directory, file_name)
            try:
                # Delete the file
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Failed to delete {file_path}: {e}")

