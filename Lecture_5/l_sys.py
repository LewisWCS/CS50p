import sys

if len(sys.argv) < 2:# in the terminal you want the file name and first name 
    sys.exit("Too few arguements") 
elif len(sys.argv) >2:
    sys.exit("Too many arguemnets")
    
    
print("Hello, my name is", sys.argv[1]) #type name in the termial when typing the code 
