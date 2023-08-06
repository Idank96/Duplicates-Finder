import pathlib, os, shutil
from pathlib import Path
from collections import defaultdict
# from zlib import crc32
from hashlib import md5


def find_duplicates(databank_paths):
    print(f'Checking for duplicate files in paths: {databank_paths}...')
    paths_dict = defaultdict(list)
    n = 0
    non_audio_files = []
    for p in databank_paths:
        for root, dirs, files in os.walk(Path(p)):
            for f in files:
                if os.path.splitext(f)[1].lower() in ['.wav', '.aif', '.aiff', '.au', '.wavex', '.flac', '.caf', '.ogg']:
                    # paths_dict[crc32(open(os.path.join(root, f), 'rb').read())].append(os.path.join(root, f)) # crc32 hash
                    with open(os.path.join(root, f), 'rb') as fp:
                        md5_hash = md5(fp.read()).hexdigest()   # md5 hash
                    paths_dict[md5_hash].append(os.path.join(root, f))
                    n += 1
                else:
                    non_audio_files.append(os.path.join(root, f))
                if n % 100 == 0:
                    print(f"\r{n:>6d} files processed ", end='', flush=True)

    duplicates = {md5: dups for md5, dups in paths_dict.items() if len(dups) > 1}
    files_in_dup_groups = sum(len(dup_group) for dup_group in duplicates.values())
    print(f"searched {n} wav/aif/aiff/au/wavex/flac/caf/ogg files for duplicates. Found {len(duplicates)} duplicate groups with {files_in_dup_groups - len(duplicates)} files to delete.")
    for dups in duplicates.values():
        print("-" * 80)
        for p in dups:
            print(p)
    print("-" * 80 + '\n')
    return duplicates


# delete the duplicate file that in the folder_identify
def del_between(duplicates, folder_identify):
    for dup_group in duplicates.values():
        for path in dup_group:
            if folder_identify in path:
                print(f'removing {path}')
                # os.remove(path)


# delete one file that is duplicate within one folder.
def del_within(duplicates, folder_identify):
    for dup_group in duplicates.values():
        for path in dup_group[:-1]:
            if folder_identify in path:
                print(f'removing {path}')
                # os.remove(path)


dir1 = r"/Users/idanko/idans_files/datasets/db_test"
# dir2 = r"C:\Users\idanko\my_scripts\Duplicates\4files_2"
folder_identify = "4files_1"


def main():
    duplicates = find_duplicates(databank_paths=[dir1])
    # del_within(duplicates, folder_identify) # put only 1 folder in the databank_paths
    # del_between(duplicates, folder_identify)
    

if __name__ == "__main__":
    main()
