import os

OS_PATH = open("sys/var/sys.cfg").readlines()[0]

def getcwd():
    path = open("sys/var/cmd.cfg").readlines()[0]
    return path 

def chdir(path):
    file = open("sys/var/cmd.cfg", "r+")
    lines = file.readlines()
    lines[0] = path
    os.remove("sys/var/cmd.cfg")
    file = open("sys/var/cmd.cfg", "w")
    file.writelines(lines)