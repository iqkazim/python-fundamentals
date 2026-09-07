from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

if len(sys.argv)==1:
    font = random.choice(figlet.getFonts())
    figlet.setFont(font=font)

elif len(sys.argv) ==3:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        if sys.argv[2] in figlet.getFonts():
            figlet.setFont(font=sys.argv[2])
        else:
            sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

s = input('Input: ')
print(figlet.renderText(s))
