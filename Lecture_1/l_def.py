def main():
    name = input("What is your name?: ").strip().title()
    hello(name)

def hello(to="world"): # define our own function so that we dont have to repeat
    print("Hello,", to)

main()
