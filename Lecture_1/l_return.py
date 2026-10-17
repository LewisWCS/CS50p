def main():
    x = int(input("What number do you want to square: "))
    print(f"This is {x} squared", square(x))

def square(n):
    return n ** 2 

main()
