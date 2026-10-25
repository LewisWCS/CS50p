# if you did pip install cowsay on your terminal
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("Hello, my name is " + sys.argv[1])