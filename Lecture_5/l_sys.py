import sys

if len(sys.argv) < 2:# in the terminal you want the file name and first name 
    print("Too few arguements") 
elif len(sys.argv) >2:
    print("Too many arguemnets")
else:
    print("Hello, my name is", sys.argv[1]) #type name in the termial when typing the code 
