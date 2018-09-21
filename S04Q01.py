""" What does this program do ?
"""

def do_action(present, redmark, bluemark):
    if present>redmark:
        print("Alarm...Please quickly close the tank valve")
    
    elif present<bluemark:
        print("Alarm...Please buy more ethanol as tank is less than 20%")
    else:
        print("Nothing to worry, you can relax !!!")

def get_current_level():
    x=input("Please Enter the Tank Current level indicator: ")
    return int(x)

# Main starts from here
capacity = 900
high = float(80/100*capacity)
low = float(20/100*capacity)
level = get_current_level()
do_action(level, high, low)
