import os
from pprint import pprint 
import time
# file manager: to see duplicate files and decide to delete or whatever
# find duplicates in a folder
    # find duplicates in all folders
    # group possible duplicates
# present duplicates to user with options: delete, etc
# user selects files and an action on the files
# perform user action: delete if user selected to delete or whatever

# containers
# Set: contains only unique items
# List: can contain duplicates, grouping may not be easy
# tuples: mutable (non-modifiable)
# dictionary: {key: value}
# listPCM = [1, 2, 3, 4, 5]
# listPCB = [6, 3, 9, 10]
# listXXXXXX = [f, fdask, fdsaa, fd, rwr]
# dictionary(listPCM: [1, 2, 3, 4, 5], listPCB: [6, 3, 9, 10], listXXXXXX = [f, fdask, fdsaa, fd, rwr], listPCM: [])
# dictionary(12343: [file1.txt, file2.java, file5.csv], 4323243:[file, file.jpg, file8.asd], 4322433: [file.djvu, file.mov, file.webm])
# dictionary(file1.txt: [/opt/projects, /opt/home/Desktop, /home/fugit/Downloads], file8.dsl: [c:\Users\halla\Documents, c:\halla_projects\webproject])
#

def getDuplicates(path, dictionary):
    for entry in os.scandir(path):
        if entry.is_file():
            # check if this file size is a key in found_files
            if dictionary.get(entry.stat().st_size):
                dictionary[entry.stat().st_size].append(entry.path)
            else:
                dictionary[entry.stat().st_size] = [entry.path]
        elif entry.is_dir():
            getDuplicates(entry.path, dictionary)

def dictionary_to_list(dictionary):
    files_list = []
    for size, files in dictionary.items():
        files_list.append("Files with size {}".format(size))
        for f in files:
            files_list.append(f)
    return files_list

# using file size as a key
def findDuplicates(path):
    found_files = {}
    getDuplicates(path, found_files)
    duplicates = {}
    for size, files in found_files.items():
        if len(files) > 1:
            duplicates[size] = files
    return duplicates

def presentDuplicateFiles(duplicate_files):
    """
    Enter number to select file to delete
    Files with size: {}
    []    --location1
    []    --location2
    []    --location3
    """
    # print duplicate files
    index = 0
    for f in duplicate_files:
        if f.startswith("Files"):
            print(f)
        else:
            print("[] {} {}".format(index, f))
        index += 1

def quit():
    print("Quiting", end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('.')
    exit(0)

# get user input
def get_user_file_choice():
    try:
        choice = input("Enter a file number to delete: ")
        choice = int(choice)
    except OSError as error:
        print("Make a wise choice: {}".format(error))
    except [ValueError, TypeError]:
        print("A number was expected.")
    finally:
        if choice:
            return choice
        return None

def delete_file(file_index, files):
    os.remove(files[file_index])

def get_user_confirmation_option():
    # handle user option
    try:
        confirm = input("Confirm to delete the file marked x: [Y/y]es/[N/n]o or q to quit: ")
    except OSError as e:
        print("Error: {}".format(e))
    finally:
        if confirm:
            if confirm[0].lower() == 'y':
                return 'y'
            elif confirm[0].lower() == 'n':
                return 'n'
            else:
                return None

def print_marked_files(choice, files):
    for index in range(len(files)):
        if files[index].startswith("Files with size"):
            print(files[index])
        else:
            marker = 'x' if index == choice else ''
            print("[{}] {} {}".format(marker, index, files[index]))

def process_file_delete(duplicates):
    duplicates = dictionary_to_list(duplicates)
    # present the files
    presentDuplicateFiles(duplicates)
    user_choice = get_user_file_choice()
    if not user_choice:
        quit()
    # print marked files
    print_marked_files(user_choice, duplicates)
    confirmation = get_user_confirmation_option()
    if not confirmation or confirmation == 'n':
        quit()
    delete_file(user_choice, duplicates)

if __name__ == '__main__':
    duplicates = findDuplicates('===========put path here===========')
    process_file_delete(duplicates)
