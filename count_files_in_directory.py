import os

def count_files_in_directory(directory):
    count = 0
    for _, _, files in os.walk(directory):
        count += len(files)
    return count