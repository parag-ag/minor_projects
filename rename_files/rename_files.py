import os

def get_files(dir):
    files_list = os.listdir(dir)
    return files_list

def rename_files(dir):
    os.chdir(dir)
    files = get_files(dir)
    print (files)
    for file in files:
        os.rename(file,file.translate(str.maketrans('','','1234567890')))
    files = get_files(dir)
    print (files)
rename_files(r"D:\Udemy")



