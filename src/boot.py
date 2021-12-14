import os
from pathlib import Path

def boot():
    # run command line
    our_path = str(Path(__file__).parent.absolute())
    cmd_path = os.path.join(our_path, "../sys/bin/")
    file = open("Jeff-OS/sys/bin/cmd")
    exec(file.read(), globals())

if __name__ == "__main__":
    boot()