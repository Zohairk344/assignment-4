from math import sqrt

def main():
    SideAB = float(input("Enter Length of side AB: "))
    SideAC = float(input("Enter length of side AC: "))
    SideBC = sqrt(SideAB**2 + SideAC**2)
    return print(f"Length of side BC is {round(SideBC, 3)}")


if __name__ == '__main__':
    main()