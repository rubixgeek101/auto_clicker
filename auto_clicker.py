"""
Clicks left mouse button every given interval
"""


#imports
import pyautogui as pag
import argparse


#argument parser
parser = argparse.ArgumentParser(description = "Clicks left mouse button repeatedly.")

parser.add_argument('-i', '--interval',
                    metavar = 'N',
                    type=float,
                    help = 'The time (sec) between each click.',
                    default = 1)

args = parser.parse_args()


n = args.interval

print('Press Ctrl-C in the console to exit.', flush = True)


#clicker
try: 
    while True:
        pag.click(interval = n)
except KeyboardInterrupt:
    print('Done.')


