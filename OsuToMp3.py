import os
from pydub import AudioSegment
import fnmatch
import re
import shutil

def convert_and_rename_mp3(file_path):
    folder_path = os.path.dirname(file_path)
    folder_name = os.path.basename(folder_path)
    clean_folder_name = re.sub(r'^\d+\s*[-]?\s*', '', folder_name)
    new_file_name = f"{clean_folder_name}.mp3"
    new_file_path = os.path.join(destination_dir, new_file_name)

    if file_path.endswith('.ogg'):
        audio = AudioSegment.from_ogg(file_path)
        audio.export(new_file_path, format='mp3')
        print(f"Converted and moved {file_path} to {new_file_path}")
    elif file_path.endswith('.mp3'):
        shutil.copyfile(file_path, new_file_path)
        print(f"Moved and renamed {file_path} to {new_file_path}")
    else:
        print(f"Unsupported file format: {file_path}")


def list_directories(base_path, pattern):
    for root, dirs, files in os.walk(base_path):
        for file_name in fnmatch.filter(files, pattern):
            file_path = os.path.join(root, file_name)
            convert_and_rename_mp3(file_path)


base_path = input("Enter the base path (where the Songs folder is located): ")
destination_dir = input("Enter the destination directory to save converted files: ")
target_file_name = "audio.*"

os.makedirs(destination_dir, exist_ok=True)

list_directories(base_path, target_file_name)
