try:
    from colorama import Fore, Back, Style
    from termcolor import colored
    OK = '['+colored("OK", "green")+']'
except:
    def colored(string, col1, col2=""):
        return string
    OK = "[OK]"