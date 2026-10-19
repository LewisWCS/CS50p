ex = input("expression: ")
x, y, z = ex.split(" ")
x = float(x)
z = float(z)

if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*" and z != 0:
    print(x * z)
elif y == "/" and z != 0:
    print(x / z)
else:
    print("Please enter valid value")