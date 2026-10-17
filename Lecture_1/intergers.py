#x = int(input("What is x?: "))
#y = int(input("What is y?: "))

x = float(input("What is x?: "))
y = float(input("What is y?: "))

z = round( y + x )
q = x / y
print(f"{z:,}")#:, in the f string just puts the number more readable using commas
print(f"{q:.2f}") # put the division is 2 decimal places

