import os
import sys
from pprint import pprint
import re
import time
import shutil
# translated, not compiled
# syntaxt
# no semicolons, no cruly braces, only indents

def is_64_bit(architecture_str):
    found = re.search(r"64", architecture_str)
    if found != None:
        return True
    return False

sysinfo = os.uname()
if not is_64_bit(sysinfo.machine):
    print('=== this program only runs in 64-bit machines ===')
    exit()

# variables_passed = sys.argv 
# name = ''
# if len(variables_passed) <= 1:
#     print('--- Usage: hello_world.py user_name ---\n Username must be specified')
#     sys.exit() # you must specify the user_name, we quit
# else:
#     print("Command line variables")
#     for var in sys.argv:
#         print(var)
#     name = sys.argv[1]
# if name:
#     print("Hello {}".format(name))
# else:
#     print("Hello World {} ".format(os.getlogin()))

# def print_hello():
#     print("Hello World")

# print_hello()
# # data types
# # Python is DYNAMICALLY typed, we don't need to specify data types for variables
# # C is statically or strongly typed: you have to specify the variable data types
# # new_module typing: an optional module to specify variable types
# age = 34
# name = "Jean"
# print("My age is "+str(age))
# def print_name():
#     print("My name is {} and my age is {}".format(name, age)) # recommended
# # control structures
# # if elif else
# age = 32
# if age == 34:
#     print_hello()
# elif age < 34:
#     print_name()
# else:
#     print("We couldn't tell your age")
# # data structures: containers
# # Lists [], tuples (), dictionary{key: value}, set: {} holds no duplicates
# files = ['hello_world.py', 'parallel.py', 'README.md', 'synch.py']
# # for f in files:
# #     print(f)
# # # lists zero-indexed and mutable
# # files[0] = 'downloader'
# # for f in files:
# #     print(f)
# # tuples: immutable
# person_details = ('Ngwada', 'Kilocha', 'Iwungilo')

# business_card = {"name": "Goodluck", "education": "JKS", "greeting": "Monili"}
# # for key, value in business_card.items():
# #     print("{}: {}".format(key, value))
# # pc_details = {"sn":"123-432N", "model": "Dell", "os": "Windowx 10", "assigned_to": "Halla"}
# # for key, value in pc_details.items():
# #     print("{}: {}".format(key, value))

# # library
# # modules os, sys


# print("My current working directory is: {}".format(os.getcwd()))
# os.chdir("/opt/projects")
# print("am now working in: {}".format(os.getcwd()))
# print("I am logged in as {}".format(os.getlogin()))


# our_set = {"Sovello", "Sovello", "Ngwada", "Ngwada", "Halla", "Halla"}
# pprint.pprint(our_set)

# pprint.pprint(sysinfo)
# print(sysinfo.machine)
# print(sysinfo.version)
# print(sysinfo.release)
# print(sysinfo.nodename)
# print(sysinfo.sysname)

# print(sysinfo.sysname)
for root, dirs, files in os.walk('/opt/Documents'):
    for directory in dirs:
        if re.search(r"venv|lib|node_modules|.git|tmp", root+"/"+directory) == None:
            for f in dirs:
                print(f)

# dictionary = {
#     'pdf': ['name.pdf', 'file2.pdf', 'file3.pdf']
#     'doc': ['name.doc', 'name2.doc', 'name3.doc']
# }


def get_file_extension(file_name):
    '''Returns the file extension or return Unknown if the file
    has no extension
    '''
    ext_re = r'\.([a-zA-Z0-9]{3})$'
    match_extension = re.findall(ext_re, file_name)
    # if match_extension:
    #     return match_extension[0]
    # return 'Unknown'
    return match_extension[0] if match_extension else 'Unknown'


def files_in_dir(dir_path):
    '''Returns a dictionary of files in a directory grouped by 
    file extensions'''
    file_dict = {}
    for entry in os.scandir(dir_path):
        if entry.is_file():
            ext = get_file_extension(entry.name)
            # check if this extension is already in the dictionary keys
            if file_dict.get(ext):
                file_dict[ext].append(entry.name)
            else:
                # create the new extension key
                file_dict[ext] = [entry.name]
    return file_dict


# Ask the user for the directory to list files
# directory = input("What directory to print files in? ")
# pprint(files_in_dir('/home/fugit/Documents'))

def directory_tree(dir_path):
    '''Prints files in a directory with indentation
    dir_path: the absolute path to the directory.
    the variable level maintains how many tabs to indent
    '''
    level = 0
    for entry in os.scandir(dir_path):
        if entry.is_dir():
            level += 1
            print("files in {}".format(entry.path))
            directory_tree(entry.path)
        else:
            print("\t"*(len(entry.path.split('/'))-5), end='')
            print(entry.name)

# directory_tree('/home/fugit/Documents')
def sorter(entry):
    '''We use this as a key to sort the directory entries
    checking whether an entry is a file (True) or not (False)'''
    return entry.is_file()


def indented_directory_tree(dir_path):
    '''
    Improves on directory_tree by automatically determining the
    indentation level
    '''
    for entry in sorted(os.scandir(dir_path), key=sorter, reverse=True):
        if entry.is_dir():
            print("files in {}".format(entry.path))
            indented_directory_tree(entry.path)
        else:
            print("\t"*(len(entry.path.split('/'))-5), end='')
            print(entry.name)

indented_directory_tree('/opt/Documents')


def files_for_backup(dir_path):
    '''
    returns a list of files (with absolute path) ready for backup.
    '''
    secs = 36*60*60
    timing = time.time()
    files_for_backup = [] # [(full_path, name), (full_path, name),]

    def check_for_backup(dir_path):
        '''checks to see if a file has been modified in the past 24 hrs.
        if it is, then it is ready for backup
        this file is added to the list of other files.'''
        for entry in os.scandir(dir_path):
            if entry.is_dir():
                check_for_backup(entry.path)
            else:
                if timing - entry.stat().st_mtime <= secs:
                    files_for_backup.append((entry.path, entry.name))
    
    check_for_backup(dir_path)

    return files_for_backup

def run_backup(dir_path):
    '''
    backs files to another directory
    '''
    destination = '/opt/backups'

    files_to_backup = files_for_backup(dir_path)
    for full_path, file_name in files_to_backup:
        shutil.copyfile(full_path, destination+'/'+file_name)

run_backup('/opt/projects/python')


# List comprehension
# entries = [entry for entry in os.scandir('/home/fugit/Documents')]
# entries = []
# for entry in os.scandir('/home/fugit/Documents'):
#   entries.append(entry)
# pprint(sorted(entries, key=sorter))