from subprocess import Popen
import sys

#filename = sys.argv[1]
while True:
    print("\nStarting " + 'visualization.py')
    p = Popen("python " + 'visualization.py', shell=True)
    p.wait()
