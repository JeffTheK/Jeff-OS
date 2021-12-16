import os
from pathlib import Path
import subprocess

# FIXME: We should probably find a better way
_dir = os.path.dirname(os.path.realpath(__file__))
_cfg = open(_dir+"/jeffos.cfg.py", "r")
OS_PATH = _cfg.readlines()[0].strip()+"/"
_cfg.close()

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

def get_current_user() -> str:
    usr_cfg = open(OS_PATH+"sys/var/usr.cfg", 'r')
    current_user = usr_cfg.readlines()[0].strip()
    usr_cfg.close()
    return current_user

def change_current_user(user_name: str):
    usr_cfg = open(OS_PATH+"sys/var/usr.cfg", 'r')
    lines = usr_cfg.readlines()
    lines[0] = user_name+"\n"
    usr_cfg.close()

    usr_cfg = open(OS_PATH+"sys/var/usr.cfg", 'w')
    usr_cfg.writelines(lines)
    usr_cfg.close()

def run_system_app(app_name, args: str):
    if args != "":
        args = args.split(" ")
    else:
        args = []
    subprocess.call([OS_PATH+"sys/bin/"+app_name] + args)
    # reload working dir
    os.chdir(getcwd())