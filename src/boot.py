import os
from pathlib import Path
from jeffos.color import OK

def boot():
    print(OK+"booting Jeff-OS")

    # run command line
    our_path = Path(__file__).parent.absolute()
    cmd_path = our_path.joinpath("sys/bin/cmd")
    cmd_path = str(cmd_path)
    file = open(cmd_path)
    exec(file.read(), globals())

if __name__ == "__main__":
    boot()