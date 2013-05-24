'''
Created on 2013-1-21

@author: liucumt
'''
#!/bin/env python
# -*- coding:utf-8 -*-
#remove .py and .py~ files from origin project
   
import os
import shutil
import compileall
from picture import settings
import stat
   
def main():    
    src_path = settings.Pro_dir
    des_path = os.path.dirname(src_path)
    des_path = os.path.join(des_path ,'newpicture')
    print src_path
    print des_path
       
#    #delete the origin source file pyc and ~ files
    for paths , _ ,files in os.walk(src_path):
        for file_name in files:
            pyc_files = os.path.join(paths,file_name)
            if os.path.exists(pyc_files):
                if pyc_files.endswith(r'.pyc') or pyc_files.endswith(r'~'):
                    os.chmod(pyc_files , stat.S_IREAD | stat.S_IWRITE)
                    os.remove(pyc_files)
                else:
                    continue
    #compile the project and produce .pyc document
    compileall.compile_dir(src_path)


#       
#    #if des_path exist then delete it
    for paths , _ ,files in os.walk(des_path):
        for file_name in files:
            file_path = os.path.join(paths , file_name)
            if os.path.exists(file_path):
                os.chmod(file_path, stat.S_IREAD | stat.S_IWRITE)
                os.remove(file_path)
            if os.path.exists(paths):
                os.chmod(paths , stat.S_IREAD | stat.S_IWRITE)
            if os.path.exists(des_path):
                shutil.rmtree(des_path)
#       
#    #copy source file to destination file
    shutil.copytree(src_path , des_path)
#       
#    #revome .py or .py~ files from destination project
    for paths , _ ,files in os.walk(des_path):
        for file_name in files:
            file_path = os.path.join(paths , file_name)
            if os.path.exists(file_path):
                if file_path.endswith(r'.py') or file_path.endswith(r'~'):
                    os.chmod(file_path, stat.S_IREAD | stat.S_IWRITE)
                    os.remove(file_path)
                else:continue
            else:
                continue
       
if __name__ == "__main__":
    main()
