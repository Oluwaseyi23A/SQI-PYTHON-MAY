# Script

# Scripts are meant to help you automate certain tasks.
import os
import shutil

# What is a module?

# A module is basically a python file. 

# This will give us a list of the names of all files and folders that we have in current folder.
all_files_in_current_folder = os.listdir('.')

# This gives us the full path of where this our current file_organizer.py file is located.
current_folder = os.getcwd()

# print("list of all files: ", all_files_in_current_folder)

# shutil.move(current_folder + '\\' + all_files_in_current_folder[0],  current_folder + '\\OTHERFOLDER\\' + all_files_in_current_folder[0] )

file_extensions_folder = {
    'Images' : ['png', 'jpg', 'jpeg'],
    'PythonFiles' : ['py'],
    'Videos' : ['mp4', 'mp3', 'mkv'],
    'Ebooks' : ['pdf', 'epub'],
    'Documents' : ['doc', 'docx'], 
    'Excel' : ['xlsx', 'xls'],

}

# Just pick every single file one by one.
for file in all_files_in_current_folder:
    ext = file.split('.')
    ext = ext[-1]
    
    for file_folder, file_extensions in file_extensions_folder.items():
        if ext in file_extensions:
            if not os.path.exists(current_folder + '\\' + file_folder):
                os.mkdir(current_folder + '\\' + file_folder)
                print('Folder did not exist but has now been created.')
        
            shutil.move(current_folder + '\\' + file , current_folder + '\\' + file_folder + '\\' + file)
            print('File moved.')
        else:
            if not os.path.exists(current_folder + '\\' + 'others'):
                os.mkdir(current_folder + '\\' + 'others')
            shutil.move(current_folder + '\\' + file , current_folder + '\\' + 'others' + '\\' + file)

    


















