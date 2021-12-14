try:
    from colorama import Fore, Back, Style
    from termcolor import colored
except:
    def colored(string, col1, col2=""):
        return string