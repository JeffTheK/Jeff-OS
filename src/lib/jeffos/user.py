from .__init__ import *
from .color import ERR

def get_current_user() -> str:
    if not os.path.isfile(OS_PATH+"sys/var/usr.cfg"):
        print(ERR+"usr.cfg not found")
        return "ERROR"
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