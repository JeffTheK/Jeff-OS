import os
from pathlib import Path

# FIXME: We should probably find a better way
OS_PATH = str(Path(__file__).parent.parent.absolute())

def getcwd():
    cfg = open(OS_PATH+"sys/var/cmd.cfg", "r")
    cwd = cfg.readlines()[0].strip()
    return cwd

def chdir(path):
    cfg = open(OS_PATH+"sys/var/cmd.cfg", "r+")
    lines = cfg.readlines()
    cfg.close()
    os.remove(OS_PATH+"sys/var/cmd.cfg")
    cfg = open(OS_PATH+"sys/var/cmd.cfg", "w")
    if path == "../":
        path = Path(path)
        lines[0] = str(path.parent.absolute())
        print("new dir ", lines[0])
    else:
        lines[0] = os.path.join(lines[0]+ path)
    cfg.writelines(lines)