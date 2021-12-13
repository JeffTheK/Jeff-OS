import os
from install import install

def boot():
    if not os.path.isdir("Jeff-OS"):
        print("Jeff-OS is not installed")
        install()