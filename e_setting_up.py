def main():
    x = input("Input: ")
    convert(x)

def convert(x):
    for vowel in "aeiouAeiou":
        x = x.replace(vowel, "")
    print(x)

main()