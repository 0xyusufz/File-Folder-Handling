from pathlib import Path
import os


def create_folder():
    try:
        f_name = input("enter a folder name you want to create:- ")
        p = Path(f_name)   # only make a path
        p.mkdir() # this actually make a folder inside path
        print("folder created successfully")
    except Exception as err:
        print(f"something went wrong {err}")

def read_file_folder():
    try:
        p = Path("")
        items = list(p.rglob("*"))
        for i,v in enumerate(items):   # enumerate return the index and value both
            print(f"{i+1}. {v} ")
    except Exception as e:
        print("something went wrong {e}")






# ============================
print("Options :- ")

print("1. Create a folder")
print("2. Read files and Folder")
print("3. Update the Folder")
print("4. Delete the Folder")
#===============================

choice = int(input("choose 1 Option "))


if choice == 1:
    create_folder()
if choice == 2:
    read_file_folder()