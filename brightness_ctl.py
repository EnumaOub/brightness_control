import os
import sys
import argparse
 

def get_display():
    display = os.popen("""sudo ddcutil detect | grep 'Display' """).read().lower().split("\n")[:-1]
    print(display)
    return display

def set_bright(args):
    dis = str(args.d)
    value = int(args.b)
    if dis == '':
        print("All Displays")
        value = int(args.b)
        if value > 100:
            value = 100
        elif value < 0:
            value = 0
        for dis in get_display():
            print(dis)
            os.system('sudo ddcutil setvcp 10 '
                    + str(value)
                    + ' --' + str(dis))
            os.system('sudo ddcutil getvcp 10 --' + str(dis))
    else:
        if value > 100:
            value = 100
        elif value < 0:
            value = 0
        print(dis)
        os.system('sudo ddcutil setvcp 10 '
                + str(value)
                + ' --' + str(dis))
        os.system('sudo ddcutil getvcp 10 --' + str(dis))




if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Script allow to control brightness"
    )
    parser.add_argument("--b", required=True, type=int, 
                        default=100, help="Enter value brightness [0-100]")
    parser.add_argument("--d", required=False, type=str, 
                        default='', help="Enter display ex: display 1")
    args = parser.parse_args()
    
    set_bright(args)
    print()