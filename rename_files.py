import os
def rename_files():
    #1. get file names from a folder
    list_files = os.listdir(r"/Users/bmaity/Downloads/prank")
    print(list_files)
    #program current working directory 
    saved_path = os.getcwd()
    print("Current working ditrecory is "+ saved_path)
    
    #changing the directory 
    os.chdir(r"/Users/bmaity/Downloads/prank")
    
    #2.for each file, rename filename
    for file_name in list_files:
        print("Old Name - "+file_name)
        print ("New name - "+file_name.translate("0123456789") )
        os.rename(file_name, file_name.translate("0123456789"))
    os.chdir(saved_path)

rename_files()
