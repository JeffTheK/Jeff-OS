#!/usr/bin/env python3

import os
import jeffos
from pathlib import Path
from jeffos.color import OK

def boot():
    print(OK+"booting Jeff-OS")

    our_path = Path(__file__).parent.absolute()

    # usr.cfg
    if not os.path.isfile(jeffos.OS_PATH+"sys/var/usr.cfg"):
        print(OK+"usr.cfg not present, installing default one")
        open(jeffos.OS_PATH+"sys/var/usr.cfg", "x")

    usr_cfg = open(jeffos.OS_PATH+"sys/var/usr.cfg", 'r+')
    if usr_cfg.read() == "":
        print(OK+"no users present, adding root user")
        usr_cfg.write("root\n") # set current user
        jeffos.run_system_app("useradd", "root")
    usr_cfg.close()

    # /tmp/
    if not os.path.isdir(jeffos.OS_PATH+"tmp/"):
        os.mkdir(jeffos.OS_PATH+"tmp/")

    # run command line
    cmd_path = our_path.joinpath("sys/bin/cmd")
    cmd_path = str(cmd_path)
    file = open(cmd_path)
    exec(file.read(), globals())

if __name__ == "__main__":
    boot()