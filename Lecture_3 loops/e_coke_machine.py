def main():
    amount_owe()

def amount_owe():
    x = 50
    while x > 0:
        z = correctcoin()
        if z > x:
            print("That coin is more than the amount remaining.")
            continue
        x = x - z
        print(x)

def correctcoin():
    while True:
        z = int(input("Please enter a coin: "))
        if z in (5, 10, 25, 50):
            return z
        else:
            print("This is not a coin")
    
main()
        








        
        
        
        