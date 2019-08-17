import os

home_directory = os.environ['HOME']

def save(filepath):
    print(f"We are saving: {filepath}")

def delete(filepath):
    print(f"We are deleting: {filepath}")