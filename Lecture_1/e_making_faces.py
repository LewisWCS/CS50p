def convert(text):
    text = text.replace(":)", "😀")
    text = text.replace(":(", "😞")
    return text
def main():
    name = input("Please tell me how you are with a :) on the end: ")
    print(convert(name))
main()