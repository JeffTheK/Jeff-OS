try:
    import colorama
    from colorama import Fore, Back, Style
    colorama.init()
except ImportError:
    print("colorama not installed, turning off color")


def turn_off_color():
    class DummyFore:
        BLACK=RED=GREEN=YELLOW=BLUE=MAGENTA=CYAN=WHITE=RESET=''
    
    saved_Fore, Fore = Fore, DummyFore