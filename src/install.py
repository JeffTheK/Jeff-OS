import os
import shutil
from datetime import datetime

def install():
    if os.path.isdir("Jeff-OS"):
        print("Jeff-OS is already installed. Replacing installation")
        shutil.rmtree("Jeff-OS")
        print("finished")

    print("starting installation")
    os.mkdir("Jeff-OS")
    os.mkdir("Jeff-OS/sys")
    os.mkdir("Jeff-OS/usr")

    print("installing default programs")
    shutil.copytree("src/bin", "Jeff-OS/sys/bin")

    print("installing libraries")
    shutil.copytree("src/lib", "Jeff-OS/sys/lib")
    os.system("cd Jeff-OS/sys/lib/ && pip install .")

    print("installing vars")
    os.mkdir("Jeff-OS/sys/var")
    os_name = "Jeff-OS"
    build_time = datetime.now()
    build_time = build_time.strftime("%Y-%m-%d %H:%M")
    actual_os_dir = os.getcwd() + "/Jeff-OS"
    sys_cfg = open("Jeff-OS/sys/var/sys.cfg", 'w')
    sys_cfg.write(actual_os_dir + "\n")
    sys_cfg.write(os_name + "\n")
    sys_cfg.write(build_time + "\n")
    sys_cfg.close()

if __name__ == "__main__":
    install()