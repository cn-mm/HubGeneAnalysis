'''
Open PlasmoDB for multiple genes entered in the command line
'''
import sys
import webbrowser
import argparse

parser = argparse.ArgumentParser(description = 'Search PlasmoDB')
parser.add_argument("usage", help = "opPlamso_sys.py {Gene1} {Gene2} {Gene3}")
args = parser.parse_args()

n = len(sys.argv)
if n <= 1: sys.exit("No gene ids read, pleas enter gene ids in command line")
 
for i in range(1, n):
    query = sys.argv[i]
    webbrowser.open('https://plasmodb.org/plasmo/app/search?q=' + query, new=2)
     