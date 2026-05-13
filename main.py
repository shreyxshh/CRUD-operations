#PROJECT1 - CRUD OPERATIONS ON FILE (USING PYTHON)
from pathlib import Path
import os

#this will tell the user if the file already exists or not
def readFileandFolder():
    """we are on the same path so no path passing
            if we've to check in another folder then pass the specific folder's path"""
    try:
        p = Path('')
        #this will take all the files in current folder and stack them together in a list
        items = list(p.rglob('*'))
        for index, file in enumerate(items):
            print(f"{index + 1} - {file}")
    except Exception as e:
        print(e)

#this will create a new file
def create_file():
    try:    
        readFileandFolder()
        file_name = input("enter your file name : ")
        p = Path(file_name)
        if p.exists():
            print("File already exists!")
        else:
            #this will create the file
            with open(file_name, 'w') as file:
                content = input("Enter your file content : ")
                file.write(content)
                print('FILE ADDED')
    except Exception as e:
        print(e)

#this will read the file requested by the user
def read_file():
    try:
        readFileandFolder()
        file_name = input("Enter your file name : ")
        p = Path(file_name)
        if p.exists():
            print("File already exists!")
            with open(file_name, 'r') as file:
                print(file.read())
        else:
            print("File not found!")
    
    except Exception as e:
        print(e)

#this will update the file as per user 
def update_file():
    try:
        print("Select file to be updated")
        readFileandFolder()
        file_name = input("Enter your file name : ")
        p = Path(file_name)
        if p.exists():
            print("press 1 to overwrite the file")
            print("press 2 to add new content at the end")
            n = int(input("Enter your choice : "))
            #overwrite condition
            if n == 1:
                with open(file_name, 'w') as file:
                    content = input("Enter content to be added : ")
                    file.write(content)
                    print('FILE UPDATED!')
            #append condition
            elif n == 2:
                with open(file_name, 'a') as file:
                    content = input("Enter content to be added : ")
                    file.write(content)
                    print('FILE UPDATED!')
            else:
                print("invalid input")
        else: 
            print('FILE DOESNT EXISTS IN THIS FOLDER!')

    except Exception as e:
        print(e)

def delete_file():
    try:
        print("Select file to deleted!")
        readFileandFolder()
        file_name = input("Enter file name : ")
        p = Path(file_name)
        if p.exists():
            os.remove(p)
        #os will completely remove the path of file from the system
            print("FILE DELETED!")
        else:
            print("file doesnt exists!")

    except Exception as e:
        print(e)

def rename_file():
    try:
        print("select the file to be renamed : ")
        readFileandFolder()
        file_name = input("enter file name : ")
        p = Path(file_name)
        if p.exists():
            new_name = input("enter new name : ")
        #path will get renamed, this action will be done by 'os'
            p.rename(new_name)
            print("FILE RENAMED!")
        else:
            print("file doesnt exist!")
    except Exception as e:
        print(e)

def create_folder():
    readFileandFolder()
    folder_name = input("enter name of your folder : ")
    p = Path(folder_name)
    if p.exists():
        print("FOLDER ALREADY EXIST!")
    else:
    # "mkdir" = make directory
    #make current folder 
        '''this will make a folder on a specific path'''
        p.mkdir()
        print("FOLDER CREATED!  ")

def remove_folder():
    readFileandFolder()
    folder_name = input("enter name of your folder : ")
    p = Path(folder_name)
    if p.exists():
        '''we dont have to specify the folder name during remova, its the only 
            path stored in the current "p" variable whose dir is being removed'''
        p.rmdir()
        # "rmdir" = remove directiory
        #remove the current folder 
        print("FOLDER REMOVED!")
    else:
        print("folder doesnt exists!")

def create_file_in_folder():
    try:
        readFileandFolder()

        print("Enter the folder name in which file is to be created")
        folder_name = input("Enter folder name : ")

        folder_path = Path(folder_name)

        # check if folder exists
        if not folder_path.exists():
            print("FOLDER DOES NOT EXIST!")
            return

        print("Enter name of file : ")
        file_name = input("Enter file name : ")

        # create complete file path
        file_path = folder_path / file_name

        # check if file already exists
        if file_path.exists():
            print("FILE ALREADY EXISTS!")
        else:
            with open(file_path, 'w') as file:
                content = input("Enter your file content : ")
                file.write(content)

            print("FILE ADDED INSIDE FOLDER!")

    except Exception as e:
        print(e)

while True:
    print("press 1 for creating a file")
    print("press 2 for reading a file")
    print("press 3 for updating a file")
    print("press 4 for deleting a file")
    print("press 5 for renaming a file")
    print("press 6 for creating a folder")
    print("press 7 for removing a folder")
    print("press 8 to create fole inside a folder")
    print("press 0 to exit")

    opt = int(input("enter your choice : "))
    if opt == 1:
        create_file()
    elif opt == 2:
        read_file()
    elif opt == 3:
        update_file()
    elif opt == 4:
        delete_file()
    elif opt == 5:
        rename_file()
    elif opt == 6:
        create_folder()
    elif opt == 7:
        remove_folder()
    elif opt == 8:
        create_file_in_folder()
    elif opt == 0:
        print("Exiting the file handling!")
        break
    else:
        print("invalid input")
        
