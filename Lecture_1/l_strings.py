name = input("Whta is your name?: ")

# This will strip the spaces left and right of the input, you can also chain
name = name.strip().title()

#This will split the first and last name into two new varibles
first , last = name.split(" ")

print(f"Hello, {first}!")