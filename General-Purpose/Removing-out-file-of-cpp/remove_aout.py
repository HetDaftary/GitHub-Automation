#!/usr/bin/env python3
import  os

to_rm = "a.out"

def traverse_path(path):
    
    global to_rm
    
    ls = os.listdir(path)

    for i in ls:
        if os.path.isdir(os.path.join(path, i)):
            traverse_path(os.path.join(path, i))
        elif i == to_rm:
            print("Target found")
            os.remove(os.path.join(path, i))

traverse_path(os.getcwd()) 