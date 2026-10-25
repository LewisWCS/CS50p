# print for vertical---------------------------------------------------------------------------------------------------------------
#def main():
    #print_column(3)
#def print_column(height):
    #for i in range(height):
        #print("#")

#main()

#prints for a row---------------------------------------------------------------------------------------------------------------
#print_row(4)

#def print_row(long):
    #print("#" * long)

#main()
def main():
    print_square(3)

def print_square(size):
    #for each row in sqaure
    for i in size:
        # for each brick in row
        print_row(size)


def print_row(width):
    print("#" * width)


main()