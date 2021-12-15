import os
from pathlib import Path

def boot():
    # run command line
    our_path = Path(__file__).parent.absolute()
    cmd_path = our_path.joinpath("sys/bin/cmd")
    cmd_path = str(cmd_path)
    file = open(cmd_path)
    exec(file.read(), globals())

if __name__ == "__main__":
    boot()