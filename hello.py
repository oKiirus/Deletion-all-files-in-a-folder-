import os 
import shutil
import time

path = input('Path: ')

files = os.listdir(path)






for i in files:

    filepath = path + '/' + i

    os.remove(filepath)

    
            
            