import random
import sys
from pyfiglet import Figlet

figlet = Figlet()

good_to_go = False

if len(sys.argv) == 3:
    if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in figlet.getFonts():
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Invalid usage")

elif len(sys.argv) == 0:
    figlet.setFont(font=random.choice(figlet.getFonts()))
else:
    sys.exit("Invalid usage")


print("Output: " + figlet.renderText(input("Input: ")))
