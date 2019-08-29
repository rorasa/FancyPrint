class FancyPrint:
    """
    Print fancy terminal output.
    Supported on all ANSI/VT100 terminal emulators.

    maintainer: Wattanit Hotrakool (@rorasa)
    """

    def __init__(self):
        self.fg_colour = {
            "black": "\033[30m",
            "red": "\033[31m",
            "green": "\033[32m",
            "yellow": "\033[33m",
            "blue": "\033[34m",
            "magenta": "\033[35m",
            "cyan": "\033[36m",
            "light_grey": "\033[37m",
            "dark_grey": "\033[90m",
            "light_red": "\033[91m",
            "light_green": "\033[92m",
            "light_yellow": "\033[93m",
            "light_blue": "\033[94m",
            "light_magenta": "\033[95m",
            "light_cyan": "\033[96m",
            "white": "\033[97m",
            "default": "\033[39m",
            "reset": "\033[39m" 
        }

        self.bg_colour = {
            "black": "\033[40m",
            "red": "\033[41m",
            "green": "\033[42m",
            "yellow": "\033[43m",
            "blue": "\033[44m",
            "magenta": "\033[45m",
            "cyan": "\033[46m",
            "light_grey": "\033[47m",
            "dark_grey": "\033[100m",
            "light_red": "\033[101m",
            "light_green": "\033[102m",
            "light_yellow": "\033[103m",
            "light_blue": "\033[104m",
            "light_magenta": "\033[105m",
            "light_cyan": "\033[106m",
            "white": "\033[107m",
            "default": "\033[49m",
            "reset": "\033[49m" 
        }

        self.style = {
            "bold": "\033[1m",
            "dim": "\033[2m",
            "underlined": "\033[4m",
            "blink": "\033[5m",
            "inverse": "\033[7m",
            "hidden": "\033[8m",
            "default": "\033[0m",
            "reset": "\033[0m"
        }

    def clear(self):
        print("\033[H\033[J", end = '')

    def reset(self):
        self.setColour('reset')
        self.setBackground('reset')
        self.setStyle('reset')

    def print(self, text):
        print(text)

    def screenPrint(self, texts):
        self.clear()
        for text in texts:
            self.print(text)

    def setColour(self, colour):
        print(self.fg_colour[colour], end = '')

    def setBackground(self, colour):
        print(self.bg_colour[colour], end = '')

    def setStyle(self, style):
        print(self.style[style], end = '')

fancy = FancyPrint()
fancy.clear()
fancy.setColour("red")
fancy.print("Hello red world!")
fancy.setBackground("blue")
fancy.setColour("white")
fancy.print("Hello blue sea!")
fancy.reset()
fancy.print("Welcome back mortals!")
