def main():
    kg = int(input("Hello we are going to find out the energy of the object please tell me the mass in KG: "))
    print(mc(kg))
def mc(mass):
    mass = mass * (300000000**2)
    return mass
main()
    