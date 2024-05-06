import os, shutil

path = r'D:/Class/'

files = os.listdir(path)

folders = []
extensions = []

#From the existing files, create folder names for each category
for file in files:
    files_split = file.split('.')
    if len(files_split) > 1:
        folder_name = files_split[1] + ' files'
        ext_name = '.' + files_split[1]
        if folder_name not in folders:
            folders.append(folder_name)
        if ext_name not in extensions:
            extensions.append(ext_name)


#creating the folders
for folder in folders:
    if not os.path.exists(path + folder):
        os.makedirs(path + folder)


#moving the files

for file in files:
    files_split = file.split('.')
    if len(files_split) > 1:
        folder = files_split[1] + ' files'
        extension = '.' + files_split[1]
        
        if extension in file and not os.path.exists(path + folder + '/' + file):
            shutil.move(path + file,path + folder + '/' + file)
print("Files moved successfully")

