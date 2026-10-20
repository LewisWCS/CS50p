def main():
    space()

def space():
    z= input("Write: ")
    for letter in z:
        if letter.isupper():
            print("_"+letter.lower(),end="")
        else:
            print(letter.lower(),end="")
    print()

main()




