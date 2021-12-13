import os
from install import install

def boot():
    if not os.path.isdir("Jeff-OS"):
        print("Jeff-OS is not installed")
        install()
    
    # run command line
    file = open("Jeff-OS/sys/bin/cmd")
    os.chdir("Jeff-OS/")
    exec(file.read(), globals())

if __name__ == "__main__":
    boot()