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