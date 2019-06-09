import os
import sys
import pprint
import re
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
for root, dirs, files in os.walk('/opt/projects'):
    for directory in dirs:
        if re.search(r"venv|lib|node_modules|.git|tmp", root+"/"+directory) == None:
            for f in files:
                if not f.startswith("."):
                    print(root+"/"+f) 
