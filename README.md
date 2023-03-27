# Duplicates-Finder
Waves Audio script

# Overview
This is a Python script that searches for duplicate files within a directory or a list of directories. It focuses on finding duplicates of audio files such as .wav, .aif, .aiff, .au, .wavex, .flac, .caf, and .ogg. The script uses the md5 hashing algorithm to compare files, and it can delete duplicate files if needed.

# Prerequisites
To run this script, you need Python 3 installed on your machine. The script uses the following built-in Python modules:

pathlib

os

shutil

collections

hashlib

# How to Use
Set the directory paths to be searched for duplicates in the databank_paths list. You can add multiple paths to the list.
If you want to delete duplicate files within a specific folder, set the folder_identify variable to the name of the folder where the duplicate files should be deleted from.
Run the script in the command line by navigating to the script's directory and typing python3 <script_name>.py. You can replace <script_name> with the actual name of the script.

# Functions
find_duplicates(databank_paths)
This function takes a list of directory paths as input and returns a dictionary where each key is a hash of a duplicate file and the value is a list of paths to the files with that hash. The function searches for audio files with extensions such as .wav, .aif, .aiff, .au, .wavex, .flac, .caf, and .ogg.

del_between(duplicates, folder_identify)
This function takes a dictionary of duplicate files and a string that identifies the folder from which the duplicate file should be deleted as inputs. It deletes one copy of each duplicate file in the identified folder.

del_within(duplicates, folder_identify)
This function takes a dictionary of duplicate files and a string that identifies the folder within which the duplicate file should be deleted as inputs. It deletes all duplicate files in the identified folder except for the last one.

main()
This is the main function that runs the script. It calls the find_duplicates function to find duplicate files in the specified directories. You can comment out the del_within or del_between function calls if you do not want to delete any files.
