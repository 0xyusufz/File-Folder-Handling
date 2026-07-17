from pathlib import Path
import os


def create_folder():
    try:
        f_name = input("enter a folder name you want to create:- ")
        p = Path(f_name)
        p.mkdir()
        print("folder created successfully")
    except Exception as err:
        print(f"somethinf went wrong {err}")


print("Options :- ")

print("1. Create a folder")
print("2. Read files and Folder")
print("3. Update the Folder")
print("4. Delete the Folder")

choice = int(input("choose 1 Option "))


if choice == 1:
    create_folder()
