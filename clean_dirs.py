import os
import glob


def remove_files(directory):
    """
    Removes all files in a directory

    Parameters:
    dir [string] = path to directory to remove all files
    """
    files = glob.glob(directory)
    for file in files:
        try:
            os.remove(file)
        except OSError as e:
            print(f"Error: {file}, {e.strerror}")
