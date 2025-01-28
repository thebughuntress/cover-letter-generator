import os
import shutil

def rm_tex_files(delete_folder=False):
    # Define the directory
    directory = os.path.join(os.getcwd(), "tex")
    try:
        # Delete the entire directory and its contents
        shutil.rmtree(directory)
        print(f"Directory deleted: {directory}")
    except Exception as e:
        print(f"Failed to delete directory {directory}: {e}")