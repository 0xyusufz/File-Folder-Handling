from pathlib import Path
import shutil
import os

while True:
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
            print(f"something went wrong {e}")

    def update_folder():
        try:
            read_file_folder()
            chose_update = input("enter a name of folder that you want to update")
            p = Path(chose_update)
            if p.exists() and p.is_dir():
                new_name = input("please tell your new name")
                new_p = Path(new_name)
                p.rename(new_p)
                print("your folder name is changes successfully")
            else:
                print("no such folder exists")
        except Exception as e:
            print(f"something went wrong as {e}")
        except Exception as e:
            print(f"something went wrong as {e}")

    def delete_folder():
        try:
            read_file_folder()
            folder_name =input("enter a name of your folder you want to delete")
            p = Path(folder_name)
            if p.exists() and p.is_dir():
                shutil.rmtree(p)
                print("folder deleted successfully")
            else:
                print("folder does not exist")
        except Exception as e:
            print(f"something went wrong as {e}")

    def create_file():
        try:
            read_file_folder()
            file_name = input("enter a file name")
            p = Path(file_name)
            if not p.exists():
                with open(file_name,"w") as f:
                    content =input("enter a content you want to write in this file or empty?")
                    if  content.lower() == "empty":
                        f.write("")
                    else:
                        f.write(content)
                print("file created successfully")
            else:
                print("file already exists")
        except Exception as e:
            print(f"something went wrong {e}")

    def read_file():
        try:
            read_file_folder()
            file_name = input("enter a file name you want to read")
            p = Path(file_name)
            if p.exists() and p.is_file():
                with open(file_name,"r") as f:
                    print("your file content is :- ")
                    print(f.read())
            else:
                print("file does not exist")
        except Exception as e:
            print(f"something went wrong{e}")

    def update_file():
        try:
            read_file_folder() 
            file_name = input("enter a file you want to update ")
            p = Path(file_name)
            if p.exists() and p.is_file():
                print("current content is :-")
                with open(file_name,"r") as f:
                    print(f.read())
                print("Options :-")
                print("1. Overwrite the data")
                print("2. Append the data")
                print("3. you want to change filename?")
                choice = int(input("choose any one option"))
                if choice == 1:
                    content = input("type your content here")
                    overwrite_data(file_name, content)
                if choice == 2:
                    content = input("type your content here")
                    append_data(file_name,content)
                if choice == 3:
                    update_file_name(file_name)
            else:
                print("file does not exist")
        except Exception as e:
            print(f"something went wrong as {e}")

    def update_file_name(old_filename):
        try:
            p = Path(old_filename)
            new_file_name = input("enter your new file name")
            p1 = Path(new_file_name)
            if not p1.exists():
                p.rename(new_file_name)
            else:
                print("file name already exist")
        except Exception as e:
            print(f"something went wrong as {e}")
    def overwrite_data(file,cont):
        try:
            with open(file,"w") as f:
                f.write(cont)
                print("content added successfully")
        except Exception as e:
            print(f"something went wrong as {e}")
    def append_data(file,cont):
        try:
            with open(file,"a") as f:
                f.write(cont)
                print("content added successfully")
        except Exception as e:
            print(f"something went wrong as {e}")


    def delete_folder_file():
        try:
            name = input("enter a file u want to delete")
            p = Path(name)
            if p.exists() and p.is_file():
                p.unlink()
                print("file deleted successfully")
            else:
                print("file doesnot exist")
        except Exception as e:
            print(f"somethinf went wrong as {e}")

    # ============================
    print("Options :- ")

    print("1. Create a folder")
    print("2. Read files and Folder")
    print("3. Update the Folder")
    print("4. Delete the Folder")
    print("5. create a file")
    print("6. Read a File")
    print("7. Update a File")
    print("8. Delete a File")
    print("0. Exit")

    #===============================

    choice = int(input("choose any one Option "))


    if choice == 1:
        create_folder()
    elif choice == 2:
        read_file_folder()
    elif choice == 3:
        update_folder()
    elif choice ==4:
        delete_folder()
    elif choice == 5:
        create_file()
    elif choice == 6:
        read_file()
    elif choice == 7:
        update_file()
    elif choice == 8:
        delete_folder_file()
    elif choice == 0:
        break
