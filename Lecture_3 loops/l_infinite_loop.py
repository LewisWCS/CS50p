#while True:
    #n = int(input("Whats n: "))
    #if n > 0:
        #break

#for i in range(n):
    #print("meow")
#----------------------------------------------------------------------------------------------------------------------------------
def main():
    number = get_number()
    meow(number)

# to get the the psotive integer from the user
def get_number():
    while True:
        n = int(input("What is n: "))
        if n > 0:
            break
    return n
# To print the amount written from the user 
def meow(n):
    for i in range(n):
        print("meow")

main()