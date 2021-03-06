import os
import shutil
import sys
import click
from datetime import datetime
from shutil import ignore_patterns

# message colors
try:
    from colorama import Fore, Back, Style
    from termcolor import colored
    OK = '['+colored("OK", "green")+']'
    WARN = '['+colored("WARN", "yellow")+']'
    ERR = '['+colored("ERR", "red")+']'
except:
    def colored(string, col1, col2=""):
        return string
    OK = "[OK]"
    WARN = "[WARN]"
    ERR = "[ERR]"

def install_default_apps():
    print(OK+"installing default programs")
    if os.path.isdir("Jeff-OS/sys/bin/"):
        shutil.rmtree("Jeff-OS/sys/bin/")
    shutil.copytree("src/bin", "Jeff-OS/sys/bin", ignore=ignore_patterns('*.c', '*.h'))

def install_default_libraries():
    print(OK+"installing libraries")

    if os.path.isdir("Jeff-OS/sys/lib/"):
        shutil.rmtree("Jeff-OS/sys/lib/")

    if os.path.isfile("src/lib/jeffos/jeffos.cfg.py"):
        os.remove("src/lib/jeffos/jeffos.cfg.py")
    
    cfg = open("src/lib/jeffos/jeffos.cfg.py", "x")
    cfg.write(os.getcwd() + "/Jeff-OS")
    cfg.close()
    shutil.copytree("src/lib", "Jeff-OS/sys/lib")
    os.system("cd Jeff-OS/sys/lib/ && pip install .")
    os.remove("src/lib/jeffos/jeffos.cfg.py")

def install():
    if os.path.isdir("Jeff-OS"):
        print(OK+"Jeff-OS is already installed. Removing old installation")
        shutil.rmtree("Jeff-OS")
        print(OK+"finished")

    print(OK+"starting installation")
    os.mkdir("Jeff-OS")
    os.mkdir("Jeff-OS/sys")
    os.mkdir("Jeff-OS/usr")

    install_default_apps()
    
    install_default_libraries()
    
    print(OK+"installing vars")
    os.mkdir("Jeff-OS/sys/var")
    # sys.cfg
    print(OK+"setting sys.cfg")
    os_name = "Jeff-OS"
    build_time = datetime.now()
    build_time = build_time.strftime("%Y-%m-%d %H:%M")
    actual_os_dir = os.getcwd() + "/Jeff-OS"
    sys_cfg = open("Jeff-OS/sys/var/sys.cfg", 'w')
    sys_cfg.write(actual_os_dir + "\n")
    sys_cfg.write(os_name + "\n")
    sys_cfg.write(build_time + "\n")
    sys_cfg.close()
    
    # cmd.cfg
    shutil.copy("src/var/cmd.cfg", "Jeff-OS/sys/var/cmd.cfg")
    cmd_cfg = open("Jeff-OS/sys/var/cmd.cfg", 'r')
    lines = cmd_cfg.readlines()
    lines.insert(0, actual_os_dir+"\n")
    cmd_cfg.close()

    cmd_cfg = open("Jeff-OS/sys/var/cmd.cfg", 'w')
    cmd_cfg.writelines(lines)
    cmd_cfg.close()

    # /dat/
    shutil.copytree("src/dat/", "Jeff-OS/sys/dat/")

    # booting and restarting
    print(OK+"copying booting files")
    shutil.copy("src/boot.py", "Jeff-OS/boot.py")

    # docs
    os.mkdir("Jeff-OS/sys/docs/")
    shutil.copy("readme.md", "Jeff-OS/sys/docs/readme.md")

@click.command()
@click.option("-bin", is_flag=True)
@click.option("-lib", is_flag=True)
def main(bin, lib):
    if len(sys.argv) <= 1:
        install()
    else:
        if bin:
            install_default_apps()
        if lib:
            install_default_libraries()

if __name__ == "__main__":
    main()