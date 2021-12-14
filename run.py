import os
from install import install

def main():
    if not os.path.isdir("Jeff-OS"):
        print("Jeff-OS is not installed")
        install()
    
    # run command line
    os.system("python Jeff-OS/boot.py")

if __name__ == "__main__":
    main()