import os
import shutil

def install():
    if os.path.isdir("Jeff-OS"):
        print("Jeff-OS is already installed. Replacing installation")
        shutil.rmtree("Jeff-OS")
        print("finished")

    print("starting installation")
    os.mkdir("Jeff-OS")
    os.mkdir("Jeff-OS/sys")
    os.mkdir("Jeff-OS/usr")

if __name__ == "__main__":
    install()