import os
import glob

def list_char_counts():
    # Get the list of files in this repo
    file_list = glob.glob('*.*')

    # Filter out the directories
    file_list = list(filter(lambda x: not os.path.isdir(x), file_list))

    # Print the table header
    print('File Name\tCharacter Count')

    # Iterate through the files
    for file in file_list:
        # Read the contents of the file
        with open(file, 'r') as f:
            contents = f.read()

        # Print the file name and its character count
        print(f'{file}\t{len(contents)}')

list_char_counts()